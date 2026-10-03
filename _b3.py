import os, re
P = r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\site\content\projects"
for f in ["cozy.md","echos.md","als.md","stormhaven.md"]:
    s = open(os.path.join(P, f), encoding="utf-8").read()
    body = s.split("---", 2)[2]
    parts = re.split(r'(?=<section )', body)
    print("="*72)
    print(f)
    out = []
    for part in parts:
        m = re.search(r'<section id="[^"]+" title="([^"]+)"', part)
        label = m.group(1) if m else "（前言）"
        txt = re.sub(r"<[^>]+>", "\n", part)
        paras = [p.strip() for p in txt.split("\n") if len(p.strip()) > 15]
        out.append((label, sum(len(p) for p in paras), len(paras)))
    for label, total, n in sorted(out, key=lambda x: -x[1]):
        bar = "#" * (total // 40)
        print("  %-32s %5d 字  %3d 段  %s" % (label[:30], total, n, bar))
