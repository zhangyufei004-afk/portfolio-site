import os, re
P = r"C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\site\content\projects"
for f in ["instance43.md","cozy.md"]:
    s = open(os.path.join(P, f), encoding="utf-8").read()
    body = s.split("---", 2)[2]
    print("="*74)
    print(f)
    print("="*74)
    # 按 section 切
    parts = re.split(r'(?=<section )', body)
    for part in parts:
        m = re.search(r'<section id="[^"]+" title="([^"]+)"', part)
        label = m.group(1) if m else "（前言）"
        txt = re.sub(r"<[^>]+>", "\n", part)
        paras = [p.strip() for p in txt.split("\n") if len(p.strip()) > 15]
        total = sum(len(p) for p in paras)
        # 找最长的几段
        top = sorted(paras, key=len, reverse=True)[:2]
        print("\n  【%s】%d 字 / %d 段" % (label, total, len(paras)))
        for t in top:
            print("     最长段 %d 字: %s..." % (len(t), t[:60]))
