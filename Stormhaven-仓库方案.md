# Stormhaven 仓库移植：分析与决定

> **已决定：采用方案 A（不移植）。** 那个空的 `zhangyufei004-afk/stormhaven` 仓库删除。
> 网站上已改为说明「仓库在校内 EngGit，项目为团队共有，客户提供基础工程与美术资产」，
> 并加了一句「如需查看具体实现可单独提供」—— 把选择权留给招聘方，而不是给一个空仓库。

---

## 你要做的两步

### 第一步：删除那个空的 GitHub 仓库

它现在是 **0 KB 的空仓库**，链接过去只会让人困惑。删除步骤：

1. 打开 https://github.com/zhangyufei004-afk/stormhaven/settings
2. 拉到最底部 **Danger Zone**
3. 点 **Delete this repository**
4. 按提示输入仓库名 `zhangyufei004-afk/stormhaven` 确认

> 删掉不影响任何东西 —— 它是空的，里面没有代码。
> 另外那个同样空的 `UE5_Combat` 也可以一并删掉或补上内容。

### 第二步：在简历里写明代码来源

你提到想写在简历上，建议这样表述（避免读起来像"代码不可查"）：

> **《风暴避难所 / Stormhaven》** — 虚幻引擎 5 探索与 FPS 游戏（校企合作项目，团队 6 人）
> 代码仓库位于坎特伯雷大学内网 EngGit，可按需提供访问；本人负责 FPS 系统与 HUD 模块。

要点是**主动说明原因**（团队共有 + 校内平台），而不是留白让人猜。

---

## 下面是当初的分析（保留备查）

### 结论

**不要整个移植。** 下面列出核实过的四个事实和三个方案。

## 一、先说三个会影响决定的事实

### 1. `hhl38/stormhaven` 不是你的仓库

从项目演示稿看，`hhl38` 是 **Shawn Leung**（团队里另一位程序员）的账号。
这个仓库是**团队共同仓库**，客户是 Tristan Leslie / Grimforge Games。

把它整体搬到 `zhangyufei004-afk` 名下，等于把别人的仓库复制成自己的。
即使团队不介意，**招聘方看到「个人账号下有一个完整团队项目」，也可能认为你在冒领** ——
这和你现在网站上把 Stormhaven 明确标为「团队项目 · 我负责 FPS 系统」是矛盾的。

### 2. 我实测过：这个 GitLab 项目当前需要登录

| 请求 | 结果 |
| --- | --- |
| `https://eng-git.canterbury.ac.nz/hhl38/stormhaven`（网页） | 200，但返回的是 **"Sign in · GitLab"** |
| `…/stormhaven.git/info/refs?service=git-upload-pack`（git 协议） | **401** |
| GitLab API `/api/v4/projects/hhl38%2Fstormhaven` | **404**（未认证时不可见） |

也就是说：**项目是私有的**，我自己无法取得它的体积。你需要登录后才能 clone。

### 3. 它大概率比你现在所有仓库加起来还大 —— 而 GitHub 有硬限制

Unreal 工程里 `Binaries/`、`Intermediate/`、`Saved/`、`DerivedDataCache/` 这几项
动辄几个 GB，而且**都不该进版本库**（`.gitignore` 一加就没了）。

对比你现有的仓库：

| 仓库 | GitHub 报告大小 | 工作区实际内容 |
| --- | --- | --- |
| `Instance-43` | **283 MB** | 约 36 MB（`Docs/` 31MB + `Assets/` 4.8MB） |
| `Cozy-Fishing` | **162 MB** | — |
| `BountyHunter` | **69 MB** | — |

注意 `Instance-43` 的数字：**工作区只有 36MB，但仓库显示 283MB** ——
差额在 **Git 历史**里。也就是说你曾经提交过一些大文件（后来删掉了），
但它们仍然留在历史中，clone 时照样要下载全部 283MB。
删文件不会让仓库变小，必须改写历史，或者重建仓库。

GitHub 免费版的硬限制是**单仓库建议 1 GB 以内**，超过会直接拒收推送。
UE5 项目带完整 `Content/` 很容易到 2–5 GB。

> **更正一处我先前的说法**：我一开始以为你仓库大是因为 `Library/` 没排除。
> 实测后发现 **`Library/` 并不在你的仓库里**（`.gitignore` 至少有排除 `Temp/`），
> 体积主要来自历史累积的大文件。给你准备的两个 `.gitignore` 模板仍然值得用，
> 但对**已经提交的历史**无效 —— 那是另一件事。

### 4. 还有一个版权层面的问题

客户提供了基础工程与「大部分美术资产」。**把客户提供的资产公开到自己的仓库**，
严格说是需要客户同意的。这一点你比我清楚，但值得先想一下。

---

## 二、三个方案

### 方案 A（推荐）：不移植，把它当**案例分析**而不是代码仓库

你网站上 Stormhaven 页已经有：**15 张实机截图、Vista 的 spline 配置、血腥屏效果、
客户问题、Playtest 反馈、完整复盘**。这一页的说服力已经**不依赖代码**。

招聘方看 UE 项目时，真正想看的是「你做了什么、怎么想的、结果如何」，
不是几百 MB 的 `.uasset` 二进制文件 —— Unreal 的资产是二进制的，
**别人 clone 下来也读不懂你的蓝图逻辑**，移植的收益远低于成本。

**具体做法：**

1. 什么都不移植。
2. 把那个**空的** `github.com/zhangyufei004-afk/stormhaven` 仓库**删掉或改名**（现在 0 KB，容易让人困惑）。
3. 网站上放一句说明（**我已经写进页面了**）：仓库在校内 EngGit，项目为团队共有，客户提供基础工程。

---

### 方案 B：只移植**你写的那部分**（如果确实想放代码）

如果招聘方明确要求看代码，那就做**精选快照**，而不是整个仓库：

```powershell
# 1. 克隆（需要你的校内账号登录）
git clone https://eng-git.canterbury.ac.nz/hhl38/stormhaven.git stormhaven-src

# 2. 在本地新建一个干净仓库，只放你负责的部分
mkdir stormhaven-fps; cd stormhaven-fps
git init
#    只复制你写的蓝图 / C++ / UI 资产，例如：
#      Content/Blueprints/FPS/
#      Content/UI/AmmoHUD/
#      Content/AI/BehaviorTrees/
#    千万不要复制：Binaries/ Intermediate/ Saved/ DerivedDataCache/ Content/（客户资产）

# 3. 写 README（说明你负责的模块 + 团队与客户分工 + 截图）
# 4. 推送
git remote add origin https://github.com/zhangyufei004-afk/stormhaven-fps.git
git add .; git commit -m "Stormhaven: FPS system and HUD (my contribution)"
git push -u origin main
```

要点：
- **务必先加 `.gitignore`**（Unreal 模板），否则又会被 `Intermediate/` 撑爆。
- 仓库改名成 `stormhaven-fps` 之类，避免和团队仓库同名造成误会。
- README 里写清「这是我在团队项目中的个人贡献，完整项目在校内 EngGit」。

---

### 方案 C：整体镜像（**我不建议**）

技术上可行：

```powershell
git clone --mirror https://eng-git.canterbury.ac.nz/hhl38/stormhaven.git
cd stormhaven.git
git push --mirror https://github.com/zhangyufei004-afk/stormhaven-mirror.git
```

但会同时踩中上面**全部四个问题**：别人的仓库、体积可能超限、客户资产、
以及「个人账号下挂着完整团队项目」的印象问题。

---

## 三、我额外建议你做的事

不管选哪个方案，有两件事收益比移植仓库更高：

### 1. 给现有仓库补 README

`BountyHunter`、`Cozy-Fishing`、`Instance-43` **全都没有 README**。
点进去是裸的工程目录，访客第一眼就流失了。每个仓库补上：

- 一句话项目简介
- **你负责什么**（团队项目尤其重要）
- 2–3 张截图
- 怎么运行 / 用哪个引擎版本打开

### 2. 清理新仓库的 `.gitignore`

Unity 项目要排除 `Library/`、`Temp/`、`Logs/`、`obj/`；
Unreal 项目要排除 `Binaries/`、`Intermediate/`、`Saved/`、`DerivedDataCache/`。
现在 `Library/` 没被排除，是你仓库偏大的主因之一。

---

## 四、需要你告诉我的

1. Stormhaven 你选 **A / B / C** 哪个？
2. 那个空的 `zhangyufei004-afk/stormhaven` 仓库要**删除**还是**改名**？
3. 要不要我给现有三个仓库**各写一份 README**（你直接复制粘贴）？
4. 要不要我写一个脚本，自动检查并生成各引擎正确的 `.gitignore`？
