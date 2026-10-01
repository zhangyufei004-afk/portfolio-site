---
slug: portal2
title: Portal 2 测试室「Interleave」
subtitle: 用传送漏斗与激光，做一间 A ⇒ B ⇒ AB ⇒ AB 的测试室
summary: 在 Portal 2 内置编辑器里设计并迭代一间四房间结构的解谜测试室。机制 A 是传送漏斗，机制 B 是激光与反射方块，第三、四间房把两者叠加成多步链式解谜。三轮迭代的核心教训是：没有环境约束，玩家一定会绕过你的谜题。
year: "2026"
type: 解谜关卡设计 · 测试室
role: 关卡设计（单人）
team: 个人项目
duration: 2026.03 – 2026.06
engine: Portal 2 PeTI 测试室编辑器
status: 已发布到 Steam 创意工坊并提交作业
tags: ["Portal 2", "解谜设计", "环境约束", "引导", "单人项目"]
cover: assets/img/portal2/cover.jpg
thumb: assets/img/portal2/cover.thumb.jpg
accent: "#f0b46b"
order: 3
---

<section id="overview" title="项目概述" kicker="Overview">
<p>
  这间测试室叫「Interleave」——名字来自它把两类机制交织在一起的方式。
  设计要求很硬性：必须在四个房间里走完 <b>A ⇒ B ⇒ AB ⇒ AB（更复杂）</b> 的结构，
  每个机制都要包含至少一个 Major Test Element，并且其中至少一个是<b>传送漏斗</b>或<b>激光</b>。
  另外明确禁用炮塔、各种凝胶、死亡泥浆等元素。
</p>
<p>
  面向的玩家不是社区里那些把 Portal 2 测试室玩到滚瓜烂熟的高手，而是一个
  <b>玩过主线、但对这间房的机制组合不熟悉</b>的普通玩家。这一点决定了谜题的难度上限。
</p>

<div class="links">
  <a class="btn btn--primary" href="https://steamcommunity.com/sharedfiles/filedetails/?id=3679048815" target="_blank" rel="noopener noreferrer">
    在 Steam 创意工坊订阅 <span class="btn__hint">↗ 站外页面（需拥有 Portal 2）</span>
  </a>
</div>

<h3>四房间结构</h3>
<div class="table-scroll">
<table>
  <thead><tr><th>房间</th><th>目的</th><th>玩家做什么</th></tr></thead>
  <tbody>
    <tr>
      <td><b>1</b></td>
      <td>引入机制 A：传送漏斗</td>
      <td>看到一道跨不过去的物理缺口 → 踩地面按钮激活传送漏斗 → 乘坐漏斗安全越过缺口</td>
    </tr>
    <tr>
      <td><b>2</b></td>
      <td>引入机制 B：激光</td>
      <td>把方块放上压力板启动激光 → 拿起反射方块，手动调整角度把光束导向接收器 → 阶梯升起</td>
    </tr>
    <tr>
      <td><b>3</b></td>
      <td>简单混合 A &amp; B</td>
      <td>目标区域步行无法抵达 → 用传送枪把激光跨过缺口折射进接收器 → 解锁传送漏斗</td>
    </tr>
    <tr>
      <td><b>4</b></td>
      <td>复杂混合 A &amp; B</td>
      <td>多步链：用传送门把方块放到压力板 → 轨道平台移动到指定位置 → 用传送门调整激光角度打开激光门 → 再把激光导向最终接收器 → 乘漏斗升上出口</td>
    </tr>
  </tbody>
</table>
</div>
</section>

<section id="concept" title="概念设计" kicker="Concept">
<h3>体验目标</h3>
<p>
  我希望玩家在解谜的过程中<b>思考空间</b>：理解不同科技元素之间如何互相作用，
  然后通过操控它们给自己清出一条路。
</p>

<h3>电梯陈述</h3>
<p>
  这是一间以<b>顺序与路由</b>为核心的空间推理测试室。整体目的是先让玩家分别学会控制
  "运动"（漏斗）与"能量"（激光），再挑战他们把两者组合起来——去操纵平台、打开门，
  并最终为自己造出一条逃生路径。
</p>

<h3>主题与场所</h3>
<p>
  经典的 Aperture Science 科幻美学：干净、无菌、高度结构化的实验室风格，
  强调功能与测试，而不是装饰。关卡发生在地下测试设施内，是一串封闭连续的测试房间，
  以白灰色面板、观察窗和深渊为主要视觉元素——深渊同时也强调了玩家必须跨越的物理缺口。
</p>

<h3>机制清单</h3>
<ul>
  <li><b>主要机制</b>：传送漏斗、激光（发射器 / 接收器 / 反射方块）</li>
  <li><b>次要机制</b>：方块、按钮（压力板）、平台（轨道平台）</li>
  <li>
    <b>我自认为比较有意思的用法</b>：最后一间房里，玩家用传送门不只是移动自己，
    而是建立一条<b>多步连锁反应</b>——触发按钮移动平台，平台移位后激光才能被路由到特定接收器，
    而最终接收器又激活了通往出口的漏斗。
  </li>
</ul>

<h3>概念评审反馈</h3>
<blockquote>
  <p>把激光和漏斗混在一起，很容易在视觉上变得非常混乱。</p>
</blockquote>
<p>
  <b>主要收获</b>：在玩家必须混合使用两种机制之前，要先用<b>玻璃面板</b>把它们在视觉上清楚地分隔开。
  这条建议直接影响了后面几个版本的房间构成方式。
</p>
</section>

<section id="iteration" title="三轮迭代" kicker="Blockout → Final">
<h3>Blockout · 玩家直接绕过了谜题</h3>
<figure class="shot">
  <img src="assets/img/portal2/blockout-a.jpg" alt="Blockout 阶段的测试室" loading="lazy" decoding="async">
  <figcaption>Blockout：目标是围绕"激光重定向"探索一套谜题</figcaption>
</figure>
<p>
  我在 blockout 阶段专注搭建一串房间，让玩家需要用传送门和激光反射方块去激活接收器来推进。
  我希望谜题包含一些垂直移动和空间思考，所以尝试了不同的平台高度与可传送表面，
  鼓励玩家抬头观察环境。
</p>
<p>
  <b>反馈</b>：最重要的意见是<b>很多玩家能跳过大量谜题</b>。
  因为可传送表面太多、限制太少，玩家经常可以在完全不触达预期机制的情况下抵达出口——
  这说明谜题的<b>约束强度不够</b>。另一个问题是部分玩家不确定主要目标是什么，
  房间里有些元素看起来是多余的，反而让谜题更不清晰。
</p>
<p>
  正面的是：玩家普遍觉得激光重定向机制有意思，说明核心想法是有潜力的。
  基于这轮反馈，下一版会聚焦<b>提升谜题清晰度</b>，并加入黑面板与
  Emancipation Grill 之类的限制来阻止玩家绕过预期解法。
</p>

<h3>Beta · 加约束，但也变得重复</h3>
<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/portal2/beta-a.jpg" alt="Beta 阶段加入不可传送表面" loading="lazy" decoding="async">
    <figcaption>加入不可传送表面，收窄解法空间</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/portal2/beta-b.jpg" alt="Beta 阶段引入光桥" loading="lazy" decoding="async">
    <figcaption>引入光桥（Light Bridge）扩展玩法可能</figcaption>
  </figure>
</div>
<p>
  <b>做了什么</b>：针对"太多可传送表面"的问题，我加入了更多限制——不可传送表面、
  调整布局以更好地把玩家导向预期解法，确保他们会按设计意图与激光机制交互。
  此外引入了光桥机制，用来创造新的位移机会，为谜题再叠加一层。
</p>
<p>
  <b>反馈</b>：玩家基本都能理解"用传送门重定向激光"这个核心机制，但有人觉得
  <b>谜题重复、缺少变化</b>，并建议增加额外的解题步骤（比如使用反射方块）来提高复杂度。
  另一个问题是部分谜题元素<b>没有清楚地传达给玩家</b>——说明需要更强的视觉引导，
  比如 antline（游戏自带的指引线）或让接收器的视线更通透。
</p>

<h3>Gamma · 过度修正成了一条走廊</h3>
<figure class="shot">
  <img src="assets/img/portal2/gamma-a.jpg" alt="Gamma 阶段的线性化布局" loading="lazy" decoding="async">
  <figcaption>Gamma：把房间重构成更线性的结构</figcaption>
</figure>
<p>
  <b>做了什么</b>：在 Gamma 阶段，我的重心转向空间精修与机制整合。复盘早期 playtest 后，
  我意识到布局太开放，玩家很容易失去对预期解谜逻辑的把握。于是我把房间重新设计得更线性、更有结构，
  让玩家自然会沿着激光与光桥谜题的推进顺序走。
</p>
<p>
  <b>反馈</b>：视觉呈现与机制执行都受到好评，但反馈指出了<b>强烈的线性感</b>。
  测试者认为房间显得又小又窄，显著降低了主动思考的必要性——因为环境太封闭，
  预期路径永远一目了然，导致缺少 Portal 2 关卡通常应有的"解谜"挑战感。
</p>
<blockquote>
  <p>这一轮是典型的过度修正：我为了解决"迷路"把空间收紧，结果把"探索"一起挤掉了。</p>
</blockquote>

<h3>Final · 放大尺度，恢复探索</h3>
<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/portal2/final-a.jpg" alt="Final 版本的测试室第 1 间" loading="lazy" decoding="async">
    <figcaption>Final：扩大第三、四间房的物理尺度</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/portal2/final-b.jpg" alt="Final 版本的激光与光桥组合" loading="lazy" decoding="async">
    <figcaption>优化谜题，消除压迫感</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/portal2/final-c.jpg" alt="Final 版本的多步链式解谜" loading="lazy" decoding="async">
    <figcaption>多步连锁：平台 → 激光 → 接收器 → 漏斗</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/portal2/final-d.jpg" alt="Final 版本的最终房间" loading="lazy" decoding="async">
    <figcaption>同时给第一间房加了机制，提高整体复杂度</figcaption>
  </figure>
</div>
<p>
  最终阶段的主要目标是解决 Gamma 测试暴露的"过于线性"与"难度过低"问题：
  扩大第三、四房间的物理尺度，优化部分谜题以消除压迫感、增强探索体验，
  同时给第一间房补充了一些机制来提高复杂度。
</p>
</section>

<section id="takeaways" title="总结与反思" kicker="Takeaways">
<h3>环境约束是谜题完整性的必要条件</h3>
<p>
  这是我在这间测试室里学到的最重要的一件事：<b>没有经过策略性布置的不可传送表面，
  玩家就一定会绕过你的设计逻辑</b>，机制设计因此贬值。
  Blockout 阶段的"玩家能跳过大量谜题"，根因不在谜题本身，而在约束不足。
</p>

<h3>空间尺度需要平衡</h3>
<p>
  Gamma 版本用窄走廊有效防止了困惑，但也同时限制住了"发现感"。
  我意识到一间成功的关卡必须<b>同时</b>提供足够的探索空间和清晰的空间线索——
  这两者不是对立的，而是需要被同时设计进去。
</p>

<div class="callout">
  <span class="callout__label">一句话</span>
  <p>引导不足会让玩家绕过谜题；约束过度会让谜题不再是谜题。</p>
</div>
</section>
