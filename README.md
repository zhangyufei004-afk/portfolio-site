# 张宇飞 · 游戏与关卡设计作品集

一个**零依赖的静态网站**。不加载任何外部资源（无 CDN、无网络字体、无统计脚本），
可以离线打开，也可以直接部署到任意静态托管平台。

- **在线地址**：（部署后填写）
- **技术形态**：纯静态 HTML + CSS + 少量原生 JS
- **站点体积**：约 25 MB（12 个页面，含作品集 PDF 与一段项目预告片）

---

## 部署

本仓库已经把**构建产物一并提交**（`dist/` 目录），所以部署时**不需要任何构建步骤**。

### 腾讯云 EdgeOne Pages（推荐，国内访问快）

1. 打开 [EdgeOne Pages 控制台](https://edgeone.cloud.tencent.com/pages)，用腾讯云账号登录
2. 选择 **从 Git 仓库导入**，绑定 GitHub，选中本仓库
3. 构建配置按下表填：

   | 配置项 | 填什么 |
   | --- | --- |
   | 框架预设 | **无 / 其他** |
   | 构建命令 | **留空** |
   | 输出目录 | `dist` |
   | Node 版本 | 随便（不构建，用不到） |

4. 点部署，几十秒后会得到一个默认域名，可直接访问

> 默认域名不需要 ICP 备案。若之后绑定自己的域名并走大陆节点，需要先完成备案；
> 走 EdgeOne 国际站或香港节点则不需要。

### Cloudflare Pages（备用 / 海外）

1. [Cloudflare Dashboard](https://dash.cloudflare.com/) → **Workers & Pages** → Create → Pages → 连接 Git
2. 构建命令**留空**，输出目录填 `dist`
3. 静态请求不计费，额度长期明确

### 任意其它静态托管

把 `dist/` 里的**全部内容**（不是 `dist` 这个文件夹本身）上传到网站根目录即可。
不需要 Node、不需要数据库、不需要服务端运行时。

Nginx 最小配置：

```nginx
server {
    listen 80;
    server_name 你的域名;
    root /var/www/portfolio;      # dist 内容所在目录
    index index.html;

    location / {
        try_files $uri $uri/ $uri/index.html =404;
    }
    location /assets/ {
        expires 30d;
        add_header Cache-Control "public, max-age=2592000";
    }
    location ~* \.(mp4|webm)$ {
        expires 30d;
        add_header Accept-Ranges bytes;   # 支持拖动进度条
    }
    gzip on;
    gzip_types text/css application/javascript image/svg+xml;
}
```

---

## 本地开发

站点由 `build.py` 生成（Python 3.8+，**不需要任何第三方包**）：

```powershell
python build.py          # 生成 dist/
```

本地预览（推荐，最接近线上效果）：

```powershell
cd dist
python -m http.server 8080
# 打开 http://127.0.0.1:8080/
```

也可以直接双击 `dist/index.html`。

### 内容怎么改

- 全局设置（站名、邮箱、Discord、SEO 描述）：`site.config.json`
- 首页与关于页：`content/index.md`、`content/about.md`
- 每个项目一页：`content/projects/*.md` —— 文件头填元信息，正文用 `<section>` 分段
- 样式 `assets/css/site.css`；脚本 `assets/js/site.js`；模板 `templates/`

**加一个新项目 = 新建一个 `.md` 文件**，作品列表会自动多出一张卡片，不需要改任何列表代码。

改联系方式时要**同时看两处**：`site.config.json`（页脚）和 `content/about.md`（关于页的"联系"章节），
否则会出现两处不一致。

详细的写法、可用的排版组件、图片与视频处理规范，见 **[`README.开发说明.md`](README.开发说明.md)**。

---

## 改完内容后的自检

`tools/` 下有四个只读的检查脚本：

```powershell
python tools/verify_site.py            # 本地链接与图片是否都能解析
python tools/lint_content.py           # 内容一致性（自相矛盾、残留占位、标签配对、字段缺失）
python tools/check_external_links.py   # 站外链接是否真的能打开（需要网络）
python tools/measure_layout.py index.html works.html   # 各断点是否横向溢出（会启动 Chrome）
```

验收标准：`broken links: 0`、`broken external links: 0`、内容问题为 0、`overflow cases: 0`。

> 这两个检查是有来历的：本站曾挂着 3 个 **404 的 GitHub 链接**（只查本地链接发现不了），
> 也出现过"移除私有仓库链接后，页面状态栏还写着**代码已开源**"这种自相矛盾 ——
> 前者由 `check_external_links.py` 兜住，后者由 `lint_content.py` 兜住。

---

## 目录结构

```
.
├── build.py                      静态站生成器（唯一需要执行的脚本）
├── site.config.json              全局设置
├── content/                      页面内容
│   ├── index.md                  首页
│   ├── about.md                  关于
│   └── projects/                 9 个项目，每个一个文件
├── templates/                    base / page / project 三个模板
├── assets/                       样式、脚本、图片、视频、可下载文档
├── tools/                        自检脚本
├── gitignore-templates/          Unity / Unreal 的 .gitignore 模板
├── dist/                         构建产物 ← 部署这个目录里的内容
├── README.开发说明.md             内容写法与部署细节
├── 口径对照表.md                  简历 / 作品集 / Wix / 本站 四个来源的口径核对
├── TODO-内容.md                   待补内容清单
└── Stormhaven-仓库方案.md         为何不移植 Stormhaven 仓库的分析
```

---

## 许可与素材说明

站内的项目截图、预告片、设计文档均为本人制作或经团队同意展示。
`assets/docs/` 下的简历与作品集 PDF 为本人所有。
第三方素材（Mixamo 动画、Unity Asset Store 资产、Pixabay 音效等）已在各项目页的
"素材与参考"章节注明来源。
