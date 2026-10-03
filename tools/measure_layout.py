"""Measure real layout widths via Chrome DevTools Protocol.

Uses a minimal WebSocket client built on the standard library only
(no third-party browser or websocket dependency).

Run from the repo root, e.g.:
    python tools/measure_layout.py index.html about.html projects/echos/index.html
"""
import base64
import json
import os
import socket
import struct
import subprocess
import sys
import time
import urllib.request
from hashlib import sha1

# Locate a Chromium browser without hard-coding a machine-specific path.
CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]
CHROME = next((c for c in CHROME_CANDIDATES if os.path.exists(c)), None)

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(SITE, ".cache-layout-check")
DIST = os.path.join(SITE, "dist")
PROFILE = os.path.join(WORK, "chromeprofile")
PORT = 9333


class WS:
    """Bare-bones WebSocket client: enough for the CDP request/response pattern."""

    def __init__(self, url, timeout=25):
        _, rest = url.split("://", 1)
        hostport, _, path = rest.partition("/")
        host, _, port = hostport.partition(":")
        self.sock = socket.create_connection((host, int(port or 80)), timeout=timeout)
        key = base64.b64encode(os.urandom(16)).decode()
        req = (
            "GET /%s HTTP/1.1\r\nHost: %s\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n"
            "Sec-WebSocket-Key: %s\r\nSec-WebSocket-Version: 13\r\n\r\n" % (path, hostport, key)
        )
        self.sock.sendall(req.encode())
        buf = b""
        while b"\r\n\r\n" not in buf:
            chunk = self.sock.recv(4096)
            if not chunk:
                raise IOError("handshake closed")
            buf += chunk
        expect = base64.b64encode(
            sha1((key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode()).digest()
        ).decode()
        if expect.lower() not in buf.decode("latin-1").lower():
            raise IOError("bad handshake")
        self.buf = buf.split(b"\r\n\r\n", 1)[1]

    def _recv_exact(self, n):
        while len(self.buf) < n:
            chunk = self.sock.recv(65536)
            if not chunk:
                raise IOError("closed")
            self.buf += chunk
        out, self.buf = self.buf[:n], self.buf[n:]
        return out

    def send(self, text):
        payload = text.encode()
        mask = os.urandom(4)
        header = bytearray([0x81])
        n = len(payload)
        if n < 126:
            header.append(0x80 | n)
        elif n < 65536:
            header.append(0x80 | 126)
            header += struct.pack(">H", n)
        else:
            header.append(0x80 | 127)
            header += struct.pack(">Q", n)
        header += mask
        masked = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
        self.sock.sendall(bytes(header) + masked)

    def recv(self):
        while True:
            b1, b2 = self._recv_exact(2)
            opcode = b1 & 0x0F
            length = b2 & 0x7F
            if length == 126:
                length = struct.unpack(">H", self._recv_exact(2))[0]
            elif length == 127:
                length = struct.unpack(">Q", self._recv_exact(8))[0]
            data = self._recv_exact(length)
            if opcode == 0x8:
                raise IOError("server closed")
            if opcode in (0x1, 0x2):
                return data.decode("utf-8", "replace")
            # ping/pong/continuation: keep reading
            continue

    def close(self):
        try:
            self.sock.close()
        except Exception:
            pass


JS = r"""
(() => {
  const de = document.documentElement;
  const vw = window.innerWidth;
  const out = { viewport: vw, scrollWidth: de.scrollWidth, offenders: [] };
  document.querySelectorAll('*').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.right > vw + 1) {
      out.offenders.push({
        tag: el.tagName.toLowerCase(),
        cls: (el.className && el.className.toString ? el.className.toString() : '').slice(0, 50),
        w: Math.round(r.width),
        right: Math.round(r.right)
      });
    }
  });
  out.offenders = out.offenders.slice(0, 8);
  return JSON.stringify(out);
})()
"""


def main():
    if CHROME is None:
        print("Chrome/Edge not found; skipping layout check.")
        return 0
    pages = sys.argv[1:] or ["index.html"]
    widths = [360, 390, 768, 1024, 1440]
    base = "file:///" + DIST.replace("\\", "/")

    os.makedirs(PROFILE, exist_ok=True)
    proc = subprocess.Popen(
        [
            CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
            "--no-first-run", "--no-default-browser-check", "--disable-crash-reporter",
            "--remote-debugging-port=%d" % PORT, "--user-data-dir=" + PROFILE,
            "about:blank",
        ],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL,
    )
    try:
        ws_url = None
        for _ in range(60):
            time.sleep(0.5)
            try:
                ws_url = json.load(urllib.request.urlopen(
                    "http://127.0.0.1:%d/json/version" % PORT, timeout=2))["webSocketDebuggerUrl"]
                break
            except Exception:
                continue
        if not ws_url:
            print("devtools unreachable")
            return 1

        ws = WS(ws_url)
        counter = [0]

        def send(method, params=None, session=None):
            counter[0] += 1
            mid = counter[0]
            msg = {"id": mid, "method": method, "params": params or {}}
            if session:
                msg["sessionId"] = session
            ws.send(json.dumps(msg))
            while True:
                obj = json.loads(ws.recv())
                if obj.get("id") == mid:
                    return obj

        bad = 0
        for page in pages:
            tid = send("Target.createTarget", {"url": "about:blank"})["result"]["targetId"]
            sid = send("Target.attachToTarget", {"targetId": tid, "flatten": True})["result"]["sessionId"]
            send("Page.enable", session=sid)
            for width in widths:
                send("Emulation.setDeviceMetricsOverride",
                     {"width": width, "height": 900, "deviceScaleFactor": 1, "mobile": width < 700},
                     session=sid)
                send("Page.navigate", {"url": base + "/" + page}, session=sid)
                time.sleep(1.4)
                res = send("Runtime.evaluate",
                           {"expression": JS, "returnByValue": True}, session=sid)
                val = res.get("result", {}).get("result", {}).get("value")
                if not val:
                    print("%-36s w=%-5d  no result" % (page, width))
                    continue
                info = json.loads(val)
                ok = info["scrollWidth"] <= info["viewport"] + 1
                if not ok:
                    bad += 1
                print("%-36s w=%-5d %-8s scrollWidth=%d" % (
                    page, width, "OK" if ok else "OVERFLOW", info["scrollWidth"]))
                for off in info["offenders"]:
                    print("          %-9s w=%-5d right=%-5d %s" % (
                        off["tag"], off["w"], off["right"], off["cls"]))
            send("Target.closeTarget", {"targetId": tid})
        ws.close()
        print("\noverflow cases: %d" % bad)
        return 1 if bad else 0
    finally:
        proc.terminate()


if __name__ == "__main__":
    sys.exit(main())
