"""Re-run extraction with PPT-aware normalization.

Two different PDF text layouts appear in these documents:
  A) one WORD per text-show operation with hard newlines (Keynote/PowerPoint export)
  B) real line-based text with headings and bullets
Detect which one a page uses and join accordingly.
"""
import sys, os, re
sys.path.insert(0, r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\.tools\wheels\pypdf.whl")
from pypdf import PdfReader

out_dir = r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\.tools\out2"
os.makedirs(out_dir, exist_ok=True)

SENT_END = re.compile(r"[.!?:;。！？：；]$")
BULLET = re.compile(r"^(?:[-•*·▪◦]|\d+[.)]|[a-z][.)]|[IVX]+\.)\s")


def segments(text):
    """Yield (kind, text) where kind is 'line' or 'blank'."""
    for raw in text.replace("\u00a0", " ").split("\n"):
        ln = re.sub(r"[ \t]+", " ", raw).strip()
        yield ("blank", "") if not ln else ("line", ln)


def normalize_page(text):
    lines = []
    blanks = 0
    for kind, ln in segments(text):
        if kind == "blank":
            blanks += 1
            continue
        if blanks:
            lines.append("")
            blanks = 0
        lines.append(ln)

    if not lines:
        return ""

    wordish = [ln for ln in lines if ln]
    if not wordish:
        return ""
    short = sum(1 for ln in wordish if len(ln) <= 14)
    ppt_style = short / len(wordish) > 0.7 and len(wordish) >= 6

    if ppt_style:
        # join everything, breaking only where the previous token ends a sentence
        out, buf = [], []
        for ln in lines:
            if ln == "":
                continue
            buf.append(ln)
            if SENT_END.search(ln) and not re.fullmatch(r"[a-z]", ln):
                out.append(" ".join(buf))
                buf = []
        if buf:
            out.append(" ".join(buf))
        return "\n".join(out).strip()

    # line-based: keep explicit newlines, but only break on blank lines when the
    # line already ends a sentence or is long enough to be a wrapped paragraph
    out, buf = [], []
    for ln in lines:
        if ln == "":
            if buf:
                out.append(" ".join(buf))
                buf = []
            if out and out[-1] != "":
                out.append("")
            continue
        if buf and (SENT_END.search(buf[-1]) or len(" ".join(buf)) > 100 or BULLET.match(ln)):
            out.append(" ".join(buf))
            buf = []
        buf.append(ln)
        if BULLET.match(ln) and len(buf) == 1:
            continue
    if buf:
        out.append(" ".join(buf))
    return "\n".join(out).strip()


for p in sys.argv[1:]:
    base = os.path.splitext(os.path.basename(p))[0]
    safe = "".join(c if (c.isalnum() or c in " -_") else "_" for c in base)[:60]
    out_path = os.path.join(out_dir, safe + ".txt")
    lines = ["", "FILE: " + os.path.basename(p)]
    try:
        r = PdfReader(p)
        lines.append("PAGES: %d" % len(r.pages))
        for i, pg in enumerate(r.pages):
            try:
                t = normalize_page(pg.extract_text() or "")
            except Exception as e:
                t = "[page error: %s]" % e
            lines.append("")
            lines.append("########## page %d ##########" % (i + 1))
            lines.append(t)
    except Exception as e:
        lines.append("ERROR: %s" % e)
    with open(out_path, "w", encoding="utf-8", errors="replace") as f:
        f.write("\n".join(lines))
    sys.stdout.write("%s\n" % out_path)
