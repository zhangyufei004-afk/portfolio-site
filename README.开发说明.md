# 个人作品集网站 · 使用说明

一个**零依赖**的静态网站：内容用普通 HTML 片段写，一条命令生成整站，
产物是纯静态文件——不加载任何外部资源，可以在本地双击打开，也可以直接上传到国内主机。

- 站名 / 邮箱 / 简介等全局设置：`site.config.json`
- 页面内容：`content/`
- 每个项目的页：`content/projects/`
- 样式：`assets/css/site.css`
- 脚本：`assets/js/site.js`
- 模板：`templates/`
- 生成器：`build.py`
- 产物（自动生成，不要手改）：`dist/`

> 另外两份**不参与构建**的工作文档：
> - `TODO-内容.md` —— 待补内容清单
> - `口径对照表.md` —— 简历 / 作品集 / Wix 站 / 本站四个来源的说法逐条对照，
>   用来确认唯一的对外口径（**建议优先处理，避免招聘方交叉比对时发现矛盾**）

---

## 一、怎么构建

需要 Python 3（3.8 以上即可，**不需要安装任何第三方包**）。

```powershell
cd C:\Users\fyhy2\Documents\deepseek-harness\default-workspace\site
python build.py
```

输出会告诉你生成了哪些文件。产物在 `dist/`：

```
dist/
  index.html              首页
  works.html              作品列表
  about.html              关于
  projects/<slug>/index.html   每个项目的详情页
  assets/css|js|img/      样式、脚本、图片
  robots.txt
  .nojekyll
```

构建过程会**先清空 `dist/`**，所以不要把手工文件放进 `dist/`。

### 为什么用 Python 生成器而不是 Astro / Next.js

1. **零依赖**：不需要 `npm install`，不需要访问境外包源，不会因为网络问题构建失败。
2. **产物干净**：没有运行时框架、没有 hydration、没有多余 JS，适合国内主机的加载环境。
3. **绝对离线**：成品连字体都不联网（用系统自带字体栈），放到哪都能秒开。

---

## 二、怎么改内容

### 改全局信息（站名、邮箱、Discord、简介、SEO 描述）

编辑 `site.config.json`，然后重新构建。其中联系方式的字段会同时出现在页脚：

```json
"email": "2485357205@qq.com",
"email_alt": "yzh440@uclive.ac.nz",
"discord": "batcat_773",
"footer_note": "..."
```

页脚模板是 `templates/base.html`；关于页的"联系"章节在 `content/about.md` 里手写 ——
改联系方式时**这两处都要看一眼**，否则会出现页脚与关于页不一致。

### 改一个项目的页面

项目页在 `content/projects/<文件名>.md`。每个文件分两部分：

**1. 文件头（front matter）** —— 用 `---` 包起来，控制卡片和页头信息：

```markdown
---
slug: echos                  ← 决定了网址 projects/echos/
title: ECHOES
subtitle: 副标题，显示在大标题下方
summary: 一句话简介，同时用于作品列表的卡片和搜索引擎描述
year: "2026"
type: 潜行恐怖 · AI 系统
role: 单人开发（设计 / 程序）   ← 这几个会出现在页头的"事实栏"
team: 个人项目
duration: 4 周
engine: Unity（C#）+ Mixamo 动画
status: 已完成的课程作业
tags: ["Unity", "有限状态机", "NavMesh"]   ← 卡片上的标签
cover: assets/img/echos/cover.jpg           ← 页头大图
thumb: assets/img/echos/cover.thumb.jpg     ← 卡片缩略图
accent: "#5ee0d0"                            ← 该页的强调色
order: 1                                     ← 作品列表里的排序，越小越靠前
---
```

**2. 正文** —— 用 `<section>` 划分章节，**每个 section 会产生一个目录条目**：

```html
<section id="overview" title="项目概述" kicker="Overview">
  <p>正文段落。</p>

  <h3>小标题</h3>
  <p>更多内容。</p>

  <figure class="shot">
    <img src="assets/img/echos/foo.jpg" alt="图片说明" loading="lazy">
    <figcaption>图注</figcaption>
  </figure>
</section>
```

- `id` 是锚点，必须唯一；`title` 是章节标题（会进右侧目录）；`kicker` 是小字英文标签，可省略。

**可用的排版组件**（直接复制使用）：

| 组件 | 写法 | 用途 |
| --- | --- | --- |
| 提示框 | `<div class="callout"><span class="callout__label">标签</span><p>内容</p></div>` | 强调一句话、说明待补充 |
| 表格 | `<div class="table-scroll"><table>…</table></div>` | 状态机、优先级、时间线等。**必须**套 `table-scroll`，否则手机上会溢出 |
| 并排图片 | `<div class="gallery gallery--2">…</div>` | 2 列（`--3` 为 3 列），小屏自动堆叠 |
| 单张带图注的图 | `<figure class="shot">…</figure>` | 点击可放大 |
| 内嵌视频 | `<figure class="video">…</figure>` | 见下面"视频怎么处理"一节 |
| 重要按钮 | `<div class="links"><a class="btn btn--primary" href="…">…</a></div>` | 站外游玩 / 订阅链接 |
| 两栏卡片 | `<div class="grid grid--2"><div class="pillar"><h3>标题</h3><p>内容</p></div>…</div>` | 并列介绍几个系统 |
| 时间线 | `<ol class="timeline">…` | 关于页已用 |

**图片路径规则**：内容里一律**从站点根目录写**（例如 `assets/img/echos/foo.jpg`），
生成器会自动补上正确的 `../` 层级。**不要**自己写 `../../`。

### 加一个新项目

1. 在 `content/projects/` 新建一个 `.md` 文件（文件名随意，`slug` 决定网址）。
2. 复制现有文件的 front matter 改掉字段，`order` 决定它在列表里的位置。
3. 把图片放进 `assets/img/<你的项目名>/`。
4. 运行 `python build.py` —— 作品列表会自动多出一张卡片，不需要改任何列表代码。

### 加一个新页面（例如"日志"或"简历"）

1. 在 `content/` 里新建 `<名字>.md`，front matter 可选（`hero_title` / `hero_sub` 会生成页头）。
2. 在 `build.py` 顶部的 `NAV` 里加一行：`("名字.html", "导航文字")`。
3. 在 `build.py` 的 `main()` 里，把 `("名字", "名字.html", "页面标题")` 加进那个 `for key, out_name, title in (...)` 列表。
4. 重新构建。

---

## 三、图片怎么处理

- 页面用的是 JPEG（体积小、兼容性最好）。原始素材（PNG / JPEG2000 等）都归档在
  素材在 `tools/image-tools/` 里有一套处理脚本，可以从原始 PDF / 录屏重新导出。
- 建议单张图**不超过 1280px 宽**、200KB 左右。当前全站图片总量约 15MB。
- 缩略图命名规则：`名字.jpg` 配一张 `名字.thumb.jpg`（卡片用）。没有 `thumb` 时会退回用 `cover`。
- 改完图片后跑一次 `python tools/verify_site.py`，它会检查每张图是否真的存在。

---

## 三点五、视频怎么处理

视频放在 `assets/media/<项目>/`，构建时会原样复制并统计体积（见构建输出的 `media/:` 那一行）。

**一定要先转码再放进去**——相机 / 录屏导出的原始文件动辄几十上百 MB，
直接上传会让页面加载变得很慢。Bounty Hunter 的预告片就是这样处理的：

```powershell
# 原始 7.5MB / 1920x1080 / 30fps  →  网页版 3.5MB / 1280x720
ffmpeg -i 原始.mp4 -c:v libx264 -profile:v high -level 4.0 -crf 25 -preset slow `
       -vf "scale=1280:-2" -c:a aac -b:a 96k -ac 2 -movflags +faststart `
       assets\media\bounty-hunter\trailer.mp4

# 从视频里抽一帧做封面图（否则播放前是黑框）
ffmpeg -ss 42 -i 原始.mp4 -frames:v 1 -vf "scale=1280:-2" -q:v 3 `
       assets\media\bounty-hunter\poster.jpg
```

关键参数说明：

| 参数 | 作用 |
| --- | --- |
| `-crf 25` | 画质与体积的平衡点。数值越小画质越好、文件越大（18 很清晰，28 开始有块） |
| `scale=1280:-2` | 缩到 1280 宽。`-2` 保证高度是偶数（H.264 要求） |
| `-movflags +faststart` | **必须加**。把索引放到文件头部，否则视频要整个下载完才能播放 |
| `-b:a 96k -ac 2` | 音频压到 96kbps 立体声，对预告片足够 |

页面里的写法（`figure.video` + `video` 组件已内置样式）：

```html
<figure class="video">
  <video class="shot" controls preload="metadata"
         poster="assets/media/项目名/poster.jpg" playsinline>
    <source src="assets/media/项目名/trailer.mp4" type="video/mp4">
    你的浏览器不支持内嵌视频播放，可以<a href="assets/media/项目名/trailer.mp4">直接下载</a>观看。
  </video>
  <figcaption>视频说明</figcaption>
</figure>
```

`preload="metadata"` 很重要：它只读取时长等元信息，**不会**在页面打开时就开始下载整个视频。

> 如果要做 GIF 动图：体积通常是 mp4 的 5–10 倍，**优先用 mp4**。
> 确实要 GIF 的话，宽度压到 640 以内、帧率降到 12–15fps。

---

## 四、部署到国内主机

产物是纯静态文件，**不需要 Node、不需要数据库、不需要任何服务端运行时**。

### 方案 A：虚拟主机 / 云服务器（推荐，最稳）

1. 把 `dist/` 里的**全部内容**（不是 `dist` 这个文件夹本身）上传到网站根目录。
2. 确保目录结构是 `网站根/index.html`、`网站根/assets/...`。
3. 服务器只需要开启静态文件服务即可。Nginx 最小配置：

```nginx
server {
    listen 80;
    server_name 你的域名;
    root /var/www/yufei-site;   # dist 内容所在目录
    index index.html;

    # 目录式网址（projects/echos/）需要能找到其中的 index.html
    location / {
        try_files $uri $uri/ $uri/index.html =404;
    }

    # 静态资源缓存（图片基本不会变）
    location /assets/ {
        expires 30d;
        add_header Cache-Control "public, max-age=2592000";
    }

    gzip on;
    gzip_types text/css application/javascript image/svg+xml;
    gzip_min_length 1024;

    # 视频不需要 gzip（已经是压缩格式），但要支持拖动进度条
    location ~* \.(mp4|webm)$ {
        expires 30d;
        add_header Cache-Control "public, max-age=2592000";
        add_header Accept-Ranges bytes;
    }
}
```

### 方案 B：对象存储 + CDN（国内：阿里云 OSS / 腾讯云 COS / 七牛）

1. 把 `dist/` 内容上传到存储桶。
2. 开启**静态网站托管**，把索引文档设为 `index.html`。
3. 目录式网址若不被支持，需要在 CDN 侧配置"目录默认首页"，或者把链接改成
   `projects/echos/index.html`（改 `build.py` 里 `project_card()` 的 `href` 即可）。
4. 记得把 `index.html` 的缓存时间设短一些（比如 5 分钟），`assets/` 设长一些。

### 方案 C：本地先看效果

直接双击 `dist/index.html` 就能在浏览器里打开，所有链接和图片都能正常显示。
不需要起本地服务器。

### 上线前的注意事项

- **ICP 备案**：如果用的是中国大陆的服务器 / 对象存储并绑定了域名，需要先完成 ICP 备案，
  否则访问会被拦截。用香港等境外节点则不需要备案，但速度稍慢。
- **HTTPS**：主流方案（云厂商证书服务、Let's Encrypt）都可以，本站无混合内容问题。
- **外链**：ECHOES 页的"素材与参考"里有 3 个维基百科 / Mixamo 外链，在国内可能打不开。
  如果想做到 100% 无境外依赖，把 `content/projects/echos.md` 里那几个 `<a href="https://...">`
  改成纯文字即可。

---

## 五、自检

改完内容后建议跑一遍这四个脚本（都在仓库的 `tools/` 下，从仓库根目录运行）：

```powershell
# 1) 本地链接与图片是否都能解析（不看网络）
python tools\verify_site.py

# 2) 内容一致性：自相矛盾的说法、残留占位、字段缺失、标签不配对
python tools\lint_content.py

# 3) 站外链接是否真的能打开（会实际请求，需要网络）
python tools\check_external_links.py

# 4) 各断点是否出现横向溢出（会启动 Chrome）
python tools\measure_layout.py index.html works.html about.html `
  projects\echos\index.html projects\als\index.html projects\portal2\index.html `
  projects\delver2d\index.html projects\stormhaven\index.html `
  projects\bounty-hunter\index.html projects\cozy\index.html `
  projects\instance43\index.html projects\vr-escaperoom\index.html
```

验收标准：`broken links: 0`、`broken external links: 0`、内容问题只剩你有意保留的项、`overflow cases: 0`。

**为什么需要第 2 和第 3 项**（都是实际踩过的坑）：

- 第 3 项：本站曾长期挂着 3 个 GitHub 链接，直到有人点开才发现是 **404** ——
  只查本地链接是发现不了的。
- 第 2 项：把私有仓库的链接移除之后，INSTANCE 43 页面的状态栏还写着"**代码已开源**"，
  页面自相矛盾。第 2 项就是为抓这一类问题写的。

> 注意：`check_external_links.py` 用 HEAD 请求，遇到 404 会自动改用 GET 复核，
> 并把 429（限流）单独列成"未能确认"而不是判为坏链接 ——
> Steam 就会对 HEAD 返回 404、对 GET 返回 200。

---

## 六、目录总览

```
site/
├── build.py                 生成器（唯一需要执行的脚本）
├── site.config.json         全局设置
├── README.md                本文件
├── content/
│   ├── index.md             首页
│   ├── about.md             关于
│   └── projects/            每个项目一个文件（当前 9 个）
│       ├── echos.md              （深度样例，内容最完整）
│       ├── instance43.md         （战斗系统策划案）
│       ├── als.md
│       ├── portal2.md
│       ├── delver2d.md
│       ├── bounty-hunter.md      （含内嵌预告片）
│       ├── cozy.md
│       ├── vr-escaperoom.md
│       └── stormhaven.md
├── templates/               base.html / page.html / project.html
├── assets/
│   ├── css/site.css
│   ├── js/site.js
│   ├── img/<项目>/           图片与缩略图
│   ├── media/<项目>/         视频与视频封面
│   └── docs/                 简历等可下载文件
└── dist/                    构建产物（上传这个目录里的内容）
```

> `assets/` 下的所有内容都会被原样复制到 `dist/assets/`。
> 所以新增一类文件（比如简历 PDF、字体、附件）只要丢进 `assets/` 任意子目录即可，
> 页面里按站点根路径引用：`<a href="assets/docs/xxx.pdf" download>`。
