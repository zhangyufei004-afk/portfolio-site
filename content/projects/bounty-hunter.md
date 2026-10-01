---
slug: bounty-hunter
title: Bounty Hunter
subtitle: 一名赏金猎人，如何变成黑市上最贵的悬赏目标
summary: 六人团队的 2D 横版动作射击游戏，可在 itch.io 直接游玩。我担任美术组的关卡与 UI 设计，负责全部关卡布局、UI 界面与背景美术。团队用一份把角色数量、音轨数量、UI 清单和"完成定义"全部写死的计划文档，来对抗范围失控。
year: "2023"
type: 2D 横版动作射击 · 叙事
role: 关卡设计与 UI 设计（美术组）
team: Stellar Studios（6 人）
duration: 2023.06 – 2023.09
engine: Unity 2D + 像素美术
status: 已发布，可在 itch.io 免费游玩
tags: ["Unity", "关卡设计", "UI 设计", "像素美术", "2D 横版", "6 人团队"]
cover: assets/img/bounty-hunter/cover.jpg
thumb: assets/img/bounty-hunter/cover.thumb.jpg
accent: "#c58ef0"
order: 6
---

<section id="overview" title="项目概述" kicker="Overview">
<p>
  《Bounty Hunter》是一款关卡驱动的 2D 横版射击（sideswiper）游戏，用独特的视角切换和原创剧情
  营造沉浸体验。玩家扮演无畏的赏金猎人 <b>Ace Cazador</b>，随着剧情推进，
  Ace 逐渐变成黑市上最昂贵的悬赏目标。
</p>
<p>
  这是一款已经<b>真正做出来并且发布出去</b>的游戏——不是原型。下文的所有画面都来自实际游戏与官方预告片。
</p>

<div class="links">
  <a class="btn btn--primary" href="https://accuratestealer.itch.io/bounty-hunter" target="_blank" rel="noopener noreferrer">
    在 itch.io 上游玩 <span class="btn__hint">↗ 站外页面</span>
  </a>
  <a class="btn" href="https://github.com/zhangyufei004-afk/BountyHunter" target="_blank" rel="noopener noreferrer">
    GitHub 仓库 <span class="btn__hint">↗ 站外页面</span>
  </a>
  <a class="btn" href="#trailer">观看预告片 ↓</a>
</div>

<h3>核心机制</h3>
<ul>
  <li>武器、近战与能力通过 Cara 的商店用金币购买，并在背包中装备。</li>
  <li>金币来自击杀敌人与 Boss 获得的升级奖励。</li>
  <li>鼠标拖拽瞄准；<b>左键</b>开火、<b>右键</b>近战、<code>E</code> 释放能力。</li>
  <li><code>W A S D</code> 控制 Ace 在关卡中移动、跑动与跳跃上平台。</li>
</ul>

<h3>HUD 传达的信息</h3>
<p>
  从官方预告片可以看到，实际游戏的 HUD 同时承担了<b>生命、弹药与 Boss 血条</b>三类信息：
  左上角是心形生命、右上角是子弹数量、屏幕中部上方是红色 Boss 血条，
  底部则是当前武器的弹药与连发状态。这套信息层级是我在关卡与 UI 设计中需要保证"看得懂、不挡视线"的部分。
</p>
<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/bounty-hunter/duel.jpg" alt="对峙画面：玩家与敌方单位同屏" loading="lazy" decoding="async">
    <figcaption>对峙瞬间：双方在同一水平面上的遭遇节奏</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/bounty-hunter/level-compound.jpg" alt="室内设施关卡中的战斗，画面右侧是 NPC 与掩体" loading="lazy" decoding="async">
    <figcaption>设施内部：掩体、箱体与 NPC 构成的可读空间</figcaption>
  </figure>
</div>
</section>

<section id="trailer" title="官方预告片" kicker="Trailer">
<p>
  47 秒的官方预告片，依次展示了开场世界观交代、室内设施遭遇、城市街道战斗、
  雪山段的平台跳跃、装备与商店界面，最后落到制作名单。页面内嵌的是转码后的版本（3.5MB），不依赖站外播放器。
</p>

<figure class="video">
  <video class="shot" controls preload="metadata"
         poster="assets/media/bounty-hunter/poster.jpg" playsinline>
    <source src="assets/media/bounty-hunter/trailer.mp4" type="video/mp4">
    你的浏览器不支持内嵌视频播放，可以<a href="assets/media/bounty-hunter/trailer.mp4">直接下载预告片</a>观看。
  </video>
  <figcaption>
    官方预告片（47 秒，1280×720）。片尾制作名单中我的署名是
    <b>BACKGROUND DESIGNER — YUFEI ZHANG</b>（另有 LEVEL DESIGN 与 UI 相关分工）。
  </figcaption>
</figure>
</section>

<section id="levels" title="关卡设计" kicker="Level Design">
<p>
  我负责的关卡设计覆盖三类差别很大的空间：自然地形、室内设施与城市环境。
  它们对平台布局、战斗空间和视觉引导的要求各不相同，这也是我在这份工作里最主要的练习内容。
</p>

<div class="gallery gallery--3">
  <figure class="shot">
    <img src="assets/img/bounty-hunter/level-mountain.jpg" alt="雪山关卡的平台跳跃段落，带 Boss 血条" loading="lazy" decoding="async">
    <figcaption><b>雪山段</b>：平台跳跃为主，顶部红色 Boss 血条说明这是场遭遇战</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/bounty-hunter/level-mountain-b.jpg" alt="雪山关卡的另一段跳跃布局" loading="lazy" decoding="async">
    <figcaption><b>雪山段（另一区段）</b>：同屏敌人、可跳平台与掩体交错</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/bounty-hunter/level-city.jpg" alt="城市关卡的垂直建筑背景与街道战斗" loading="lazy" decoding="async">
    <figcaption><b>城市段</b>：垂直堆叠的建筑背景，营造纵深</figcaption>
  </figure>
</div>

<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/bounty-hunter/level-compound-b.jpg" alt="设施与雪山交界处的推进段落" loading="lazy" decoding="async">
    <figcaption><b>推进段</b>：从室内向户外过渡，用落差交代路线方向</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/bounty-hunter/level-compound.jpg" alt="室内设施关卡的战斗空间与掩体" loading="lazy" decoding="async">
    <figcaption><b>设施段</b>：横向走廊 + 掩体，战斗与推进合一</figcaption>
  </figure>
</div>

<h3>我在关卡设计上的取舍</h3>
<ul>
  <li>
    <b>用平台高度说话</b>：雪山段几乎不靠文字或箭头引导，而是让可跳平台的高度差本身构成一条
    "看得见的路线"——玩家一眼就能判断哪里能上去。
  </li>
  <li>
    <b>战斗空间要留横向余地</b>：因为是横版射击，敌人会持续追击，
    所以设施段我刻意保留了可后退的走廊宽度，避免玩家被逼进无法拉开距离的角落。
  </li>
  <li>
    <b>背景要承担氛围但不抢戏</b>：城市段的建筑背景层数很多，我需要在"够丰富"和
    "不干扰玩家辨识前景平台"之间反复调整对比度。
  </li>
</ul>
</section>

<section id="ui" title="UI 与背景美术" kicker="UI &amp; Art">
<p>
  UI 设计是我在这份工作里优先级判断最明确的一块：角色与动画是驱动整个游戏的美术主干（预计 2–3 周），
  图标 / UI 本身最容易做（不到一周），但它<b>必须与关卡设计同步做</b>——
  否则最后一定会出现"界面像贴上去的"这种协调问题。这也是我在计划阶段就提出的协作要求。
</p>

<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/bounty-hunter/ui-shop.jpg" alt="Cara The Shopkeeper 角色卡片界面" loading="lazy" decoding="async">
    <figcaption><b>Cara The Shopkeeper</b>：商店 NPC 的角色卡片，像素立绘 + 场景背景</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/bounty-hunter/ui-equipment.jpg" alt="装备与道具槽界面" loading="lazy" decoding="async">
    <figcaption><b>装备 / 道具面板</b>：槽位、绿色可用状态与数值区</figcaption>
  </figure>
</div>

<h3>角色卡片的设计考虑</h3>
<p>
  这类"角色登场卡片"要在一屏内完成两件事：<b>建立角色身份</b>（名字 + 立绘 + 站位）
  和<b>铺垫场所</b>（背景里的店铺陈设）。所以我用对称的构图和统一的像素描边，
  让卡片无论出现在哪一关都能保持同一套视觉语言——这也是"UI 必须与关卡同步设计"的直接体现。
</p>

<h3>声音的设计意图</h3>
<p>
  音效覆盖武器、机制、脚步、受伤、环境音、不同兵种的声音（用于在战斗中辨识敌人）以及能力音效。
  目标是让每种声音都承担信息功能——<b>用声音帮玩家判断战场上正在发生什么</b>。
  配乐方向是经典间谍 / 动作主题 + 未来感音色 + funk 的混合，可能更偏向摇滚。
</p>
</section>

<section id="role" title="我的职责与团队分工" kicker="Role">
<p>
  团队分为三组：<b>美术组</b>（Max 与我）、<b>程序组</b>（Jacob、Nic）、
  <b>叙事与文档 / 视频组</b>（Geordie、Liam）。Max 担任队长，负责角色设计与动画、音乐与音效；
  我负责<b>关卡设计、UI 与背景美术</b>。
</p>

<div class="table-scroll">
<table>
  <thead><tr><th>交付物</th><th>我的工作</th><th>依赖关系</th></tr></thead>
  <tbody>
    <tr>
      <td>关卡设计</td>
      <td>设计角色穿行的关卡布局：平台分布、移动路线、战斗空间与遭遇节奏</td>
      <td>依赖程序组实现移动与敌人功能；依赖叙事组给出每关对应的剧情段落</td>
    </tr>
    <tr>
      <td>UI 与图标</td>
      <td>地图、商店 / 装备、主菜单与游戏内 HUD 的界面与图标设计</td>
      <td>需要与程序组协作确保能被实现；与关卡设计保持视觉一致</td>
    </tr>
    <tr>
      <td>背景美术</td>
      <td>各关卡的背景，质量需与角色动画相匹配以保持整体协调</td>
      <td>依赖叙事组确定每关的场所与氛围</td>
    </tr>
  </tbody>
</table>
</div>

<h3>制作与协作方式</h3>
<ul>
  <li><b>Discord</b>：general 频道用于日常沟通，dev-log 频道用于各自同步任务进度。</li>
  <li><b>Trello</b>：按板块分列（美术 / UI / 程序 / 叙事 / 提交物 / 杂项），另有 doing 与 done 两列。</li>
  <li><b>OneDrive</b>：按类型分文件夹（背景、角色精灵与动画、文档、音乐、叙事、程序文件、音效、UI 素材）。</li>
  <li><b>会议</b>：固定在每周 workshop 时间，所有人同时在场。</li>
  <li>
    <b>每周目标制</b>：每人（或每组）在每周结束时达成一个明确目标，并且必须说清楚
    <b>自己的进度如何影响、如何接入其他人的工作</b>——这条规则的实际作用是把"我做完了"
    变成"我这部分接得上别人"。
  </li>
</ul>
</section>

<section id="scope" title="范围控制" kicker="Scope Control">
<p>
  计划文档里我们把"完成"拆到可计数的程度，这是我在这个项目里认为最有效的一个做法：
</p>
<div class="table-scroll">
<table>
  <thead><tr><th>板块</th><th>量化的完成标准</th></tr></thead>
  <tbody>
    <tr><td>美术</td><td>6 名主要角色 + 3 名次要角色；角色之间动画各不相同；商店 / 地图 / 主菜单 / 游戏内 HUD 的图标与 UI</td></tr>
    <tr><td>声音 / 音乐</td><td>4 首配乐（对应各主要角色的关卡）+ 每个物理动作的音效（射击、跑动、受击、跳跃等）</td></tr>
    <tr><td>程序</td><td>所有功能按预期工作、尽量少 bug、不造成卡顿或崩溃，且整体玩法风格统一、不显得东拼西凑</td></tr>
    <tr><td>叙事</td><td>故事线连贯、对白符合既定角色性格、与关卡中建立的故事一致</td></tr>
  </tbody>
</table>
</div>

<h3>风险与预案</h3>
<ul>
  <li>
    <b>最大风险是"不是每个人都跟上自己的任务与截止"</b>。缓解方式是通过 Trello 与 Discord 主动同步进度，
    并在跟不上时提前告知；所有素材放在共享 OneDrive 里。
  </li>
  <li>
    <b>范围失控</b>：我们在计划阶段就已经从最初的构想里砍掉了一部分，并预留了进一步收缩的方案——
    例如<b>第五关可以被整体删掉</b>以应对时间不足；非必要的游戏元素只在核心元素完成并打磨好之后才做。
  </li>
  <li>
    <b>过场动画的降级预案</b>：如果时间不够，过场可以简化成一张静帧 + 一段滚动的对白。
  </li>
</ul>
<p class="dim">
  我们明确写下了"从《Expressing the Ordinary》那个项目学到的教训是：沟通是按时完成项目的关键"。
  这条经验在后来所有团队项目里都反复被验证。
</p>
</section>

<section id="takeaways" title="反思" kicker="Takeaways">
<h3>把"完成"写成数字，是控制范围最有效的动作</h3>
<p>
  6 个主角色、3 个次角色、4 首配乐、4 套 UI 界面——这些数字看起来机械，
  但它们让"我们做得够不够"变成了一个可以互相核对的问题，而不是各自感觉。
  这也是我在后面《Cozy Fishing》和《Stormhaven》里持续沿用的做法。
</p>

<h3>跨职能的接口必须提前约定</h3>
<p>
  我在计划阶段就写明"图标 / UI 必须与关卡设计协作，确保一切都在游戏里成立"，
  原因是美术资产如果各做各的，最后一定会出现风格与功能上的拼接感。
  <b>提前约定接口，比事后统一风格便宜得多。</b>
</p>

<h3>降级预案要写进计划，而不是临时决定</h3>
<p>
  "第五关可以整关砍掉""过场可以降级成静帧"这两条预案写下来之后，
  团队在面对时间压力时就不需要再做一次痛苦的取舍讨论——决策成本被提前支付了。
</p>

<h3>最终结果</h3>
<p>
  游戏完成并发布到 itch.io，任何人都可以直接游玩；预告片的制作名单里也保留了完整的团队署名。
  对我来说，这个项目最大的收获不是"做出了一个游戏"，
  而是学会了<b>怎么把创意约束进一个六个人能真正交付的范围里</b>。
</p>
</section>
