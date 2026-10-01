"""Extract text from a .docx (OOXML zip) with the standard library only."""
import sys, zipfile, re, os

src = sys.argv[1]
out = sys.argv[2]

with zipfile.ZipFile(src) as z:
    names = z.namelist()
    xml = z.read("word/document.xml").decode("utf-8", "replace")

# paragraphs: split on </w:p>, tabs/breaks -> spaces
paras = re.split(r"</w:p>", xml)
lines = []
for p in paras:
    texts = re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, re.S)
    txt = "".join(texts)
    txt = re.sub(r"<[^>]+>", "", txt)
    txt = (txt.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
              .replace("&quot;", '"').replace("&apos;", "'"))
    txt = re.sub(r"[ \t]+", " ", txt).strip()
    # detect table rows for a rough hint
    if txt:
        lines.append(txt)

body = "\n\n".join(lines)
with open(out, "w", encoding="utf-8") as f:
    f.write("FILE: %s\nPARAGRAPHS: %d\n\n%s" % (os.path.basename(src), len(lines), body))
print("chars:", len(body), "->", out)
