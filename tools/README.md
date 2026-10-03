# tools — 自检与素材处理脚本

两个子目录，用途不同。所有脚本都**从仓库根目录**运行，路径由脚本自身位置解析。

## 一、自检脚本（改完内容后跑）

```powershell
python tools/verify_site.py            # 本地链接与图片是否都能解析（不看网络）
python tools/lint_content.py           # 内容一致性：自相矛盾、残留占位、字段缺失、标签配对
python tools/check_external_links.py   # 站外链接是否真的能打开（需要网络）
python tools/measure_layout.py index.html about.html projects/echos/index.html
                                       # 各断点是否横向溢出（需要 Chrome/Edge）
```

验收标准：`broken links: 0`、`broken external links: 0`、内容问题为 0、`overflow cases: 0`。

两个提醒：

- `verify_site.py` 遇到站外链接会**列出来并返回 1**，这是设计如此（它只负责本地路径）。
- `check_external_links.py` 会先发 HEAD 请求，失败时改用 GET 复核，并把 **429（限流）**
  单列为"未能确认"而不是判为坏链接 —— Steam 就对 HEAD 返回 404、对 GET 返回 200。

## 二、素材处理脚本（`image-tools/`，偶尔才需要）

这些脚本把原始素材（PDF、录屏、视频）转成网页用的图片。
它们依赖第三方库（`pypdf`、`Pillow`）和 `ffmpeg`，**构建网站本身不需要它们** ——
`build.py` 只用 Python 标准库。

| 脚本 | 用途 |
| --- | --- |
| `extract2.py` | 从 PDF 提取正文，按版面智能合并断行 |
| `docx_text.py` | 从 `.docx` 提取正文（标准库解 OOXML，不需要 python-docx） |
| `convert_images.py` / `convert_portfolio_images.py` | 把提取出的配图转成网页格式，并生成缩略图 |
| `resize_images.py` | 批量压到 1280px 宽、JPEG q76（全站从 89MB 压到 15.6MB） |
| `extract_trailer_frames.py` | 从预告片抽帧，**带亮度断言**（防止抽出黑帧当封面） |
| `detect_gameview.py` | 用亮度剖面**实测**录屏里游戏视图的精确边界，用于裁掉编辑器界面 |
| `extract_vr_frames.py` | 按上一步测出的边界从 VR 录屏抽帧 |
| `make_placeholder_covers.py` | 给还没素材的项目生成明确标注的占位封面 |

### 为什么抽帧脚本要带亮度断言

Bounty Hunter 的预告片里有多段纯黑标题卡。第一版抽帧脚本没有校验，
结果把一张黑帧当成了封面 —— 页面上就是一大块黑。

现在 `extract_trailer_frames.py` 会计算每帧平均亮度，低于阈值直接报错退出；
`extract_vr_frames.py` 同理。这类"看起来没问题但实际是空的"素材，
比明显报错更难发现。

### 一个踩过的坑

用 `fps=1/3 + tile=4x4` 生成的缩略拼图来定位画面时间点是**不可靠的** ——
拼图里的第 N 格并不对应精确的 N×3 秒。定位时间点应该逐秒采样并标注时间戳，
不要靠拼图反推。
