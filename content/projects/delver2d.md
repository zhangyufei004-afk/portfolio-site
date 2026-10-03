---
slug: delver2d
title: 塞尔达式 2D 地牢「Delver」
subtitle: 用抓钩与推块讲一道空间谜题，而不是用敌人
summary: 在课程自研的 2D 地牢关卡编辑器里制作，以初版《塞尔达传说》的地牢为参照。核心是把战斗导向的设计改成环境导向：抓钩 + 可推方块是主谜题机制，钥匙与锁门控制节奏，传送器绕开岩浆。五个阶段的 playtest 迭代最终把重点从"更复杂"转成了"永不让玩家卡死"。
year: "2026"
type: 2D 地牢关卡设计
role: 关卡设计（单人）
team: 个人项目
duration: 2026.03 – 2026.06
engine: Unity + 课程自研 2D 地牢关卡编辑器
status: 已完成课程作业
tags: ["关卡设计", "2D 地牢", "空间解谜", "抓钩", "节奏控制", "单人项目"]
cover: assets/img/delver2d/cover.jpg
thumb: assets/img/delver2d/cover.thumb.jpg
accent: "#e0c25e"
order: 4
---

<section id="overview" title="项目概述" kicker="Overview">
<p>
  这是用课程自研的 2D 地牢关卡编辑器制作的关卡，设计上以初版《塞尔达传说》的地牢为参照。
  它在设定上<b>不是游戏的第一座地牢</b>，而是<b>抓钩（Grappler）首次登场</b>的地方：
  玩家应该在没有抓钩的状态下走过大约三分之一的关卡，然后拿到它，之后面对几道难度递增的抓钩谜题。
</p>

<h3>体验目标</h3>
<p>
  我想让玩家通过探索与空间解谜获得<b>成就感</b>——先用仔细的探索克服最初的"人为难度"感，
  最终过渡到顺畅、满足的推进节奏。
</p>

<h3>电梯陈述</h3>
<p>
  一关参照初版《塞尔达传说》的地牢探索关。核心体验依赖<b>策略性探索</b>——
  用有限的资源（钥匙）和独特的位移机制推进，而不是用敌人把玩家淹没。
  它提供公平且有趣的解谜挑战，鼓励玩家在脑中先画出空间地图。
</p>

<h3>主题与场所</h3>
<p>
  经典复古地牢 / 神庙。环境由彼此区分的房间构成，并用环境危险（岩浆）来封路，
  逼迫玩家用特定的位移手段绕过。
</p>

<h3>用到的机制</h3>
<ul>
  <li>
    <b>抓钩 + 可推方块</b>（核心谜题机制）：玩家会遇到<b>无法从反方向推动</b>的方块，
    必须自己发现"可以用抓钩穿过这些方块"才能推进。
  </li>
  <li>
    <b>钥匙与锁门</b>：大量用于控制节奏与推进。钥匙散落在关卡各处（包括像第三间房这样的早期区域），
    却用来打开路径远端的门。
  </li>
  <li>
    <b>传送器</b>：作为位移工具，用来绕开岩浆这类环境危险，并连接地图的不同区域。
  </li>
</ul>

<figure class="shot">
  <img src="assets/img/delver2d/macro.jpg" alt="Delver 关卡的 Macro Chart" loading="lazy" decoding="async">
  <figcaption>Macro Chart：把层级、时长、情绪、机制与敌人需求排成一行——先定节奏再定布局。</figcaption>
</figure>
</section>

<section id="iteration" title="四个阶段的迭代" kicker="Blockout → Final">
<p>
  这一关经历 Blockout / Alpha / Beta / Final 四个阶段，每一轮 playtest 都改变了我对"问题在哪"的判断。
</p>

<h3>Blockout · 迷路、回头路与敌人密度</h3>
<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/delver2d/blockout-a.jpg" alt="Blockout 阶段的关卡布局" loading="lazy" decoding="async">
    <figcaption>Blockout：把玩法重心从战斗转向环境位移与空间解谜</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/delver2d/blockout-b.jpg" alt="Blockout 阶段的房间与传送器分布" loading="lazy" decoding="async">
    <figcaption>围绕抓钩与推块建立协同关系，玩家必须与地形互动才能推进</figcaption>
  </figure>
</div>
<p>
  Blockout 阶段做的关键决定，是把体验从<b>重战斗</b>转向<b>环境位移与空间解谜</b>，
  并把关卡设计围绕"抓钩 + 推块"的协同建立起来。
</p>
<p>
  <b>反馈</b>：抓钩机制与以地形为核心的谜题被认为是极有创意且吸引人的，
  但关卡存在严重的<b>导航与引导问题</b>。最关键的一条是<b>令人沮丧的回头路</b>：
  玩家常常走到关卡末端才发现自己漏了第三间房里的关键钥匙，只能把整张地图再走一遍。
  此外多名测试者表示<b>因为缺少明确方向而"迷路"</b>，
  这部分被错放的传送器和需要非直觉解法的谜题（比如用抓钩穿过方块）进一步放大了。
</p>
<p>
  我也学到<b>敌人密度过高</b>会让关卡显得"人为地难"。
</p>

<h3>Alpha · 挪动钥匙房 + 编号锚点</h3>
<figure class="shot">
  <img src="assets/img/delver2d/alpha-a.jpg" alt="Alpha 阶段的关卡布局" loading="lazy" decoding="async">
  <figcaption>Alpha：钥匙房被移动到抓钩获取点旁边，并加入编号标记</figcaption>
</figure>
<p>
  <b>改动</b>：把钥匙房从第三间房挪到紧邻抓钩获取点，解决"过度回头路"；
  并在全图加入<b>数字编号</b>辅助导航。
</p>
<p>
  <b>反馈</b>：推进变得"非常清晰"，传送门方块与"用抓钩触发压力板"获得好评；
  但测试者仍觉得敌人太多，明确指出 <b>Boss 房像一个"敌人堆砌场"</b>，分散了对谜题的注意力。
  另外，「带着钥匙的骷髅在玩家身后生成」这类事件需要更好的视听提示，否则容易被错过。
</p>

<h3>Beta · 削减敌人，但暴露了卡死风险</h3>
<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/delver2d/beta-before.jpg" alt="Beta 之前的关卡布局" loading="lazy" decoding="async">
    <figcaption>Beta 之前</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/delver2d/beta-after.jpg" alt="Beta 之后的关卡布局" loading="lazy" decoding="async">
    <figcaption>Beta 之后：削减敌人，用推块与压力杆组合替代刷怪</figcaption>
  </figure>
</div>
<p>
  <b>改动</b>：针对"敌人堆砌"重排战斗与解谜的配比 —— 第二间房移除两个刷怪点，
  改成<b>推块 + 压力杆</b>组合；把普通门替换成<b>清光敌人才开锁</b>的房间锁；
  在减少总量的同时提高剩余遭遇的威胁度。
</p>
<p>
  <b>反馈</b>：暴露了两个更严重的问题。一是<b>很高的卡死风险</b>——
  测试者被困在<b>有锁门但没有钥匙</b>的房间里，又无法回到之前的区域找钥匙；
  二是数字标记<b>并不直观</b>，玩家不理解它的含义。部分测试者因此没能完整通关。
</p>
<blockquote>
  <p>这轮结果明确了一件事：必须保证在关键目标达成之前路径始终是开放的，并且导航系统需要更清晰的视觉提示。</p>
</blockquote>

<h3>Final · 把"逻辑安全"放在复杂度之上</h3>
<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/delver2d/final-before.jpg" alt="Final 之前的关卡布局" loading="lazy" decoding="async">
    <figcaption>Final 之前</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/delver2d/final-after.jpg" alt="Final 之后的关卡布局" loading="lazy" decoding="async">
    <figcaption>Final 之后：重构返回路径，保证永远不会被卡住</figcaption>
  </figure>
</div>
<p>
  最终阶段我把重心从"机制能用"转到"体验被打磨"：
</p>
<ul>
  <li>针对 Beta 暴露的卡死风险，我对<b>所有钥匙与门的位置做了一次完整审查</b>。</li>
  <li>核心决定是<b>把"逻辑安全"的优先级放在复杂度之上</b>：重构返回路径，
    确保即使玩家漏掉了某个道具，也永远不会被困住、总有路可以回头。</li>
  <li>改进编号引导系统。我的意图不只是给房间贴标签，而是把这些标记当成
    <b>"视觉锚点"</b>来澄清解谜顺序。</li>
  <li>继续处理"敌人堆砌"的通病：用有意图的、更高质量的遭遇替换杂乱刷怪。
    例如在"压力杆"这类房间里，我有策略地布置敌人来配合谜题的节奏，
    让它们成为有意义的关卡障碍，而不是挫败感的来源。</li>
</ul>
<p>
  这个过程让我明白：<b>设计师的工作是保护玩家的心流，和挑战玩家的心流同样重要。</b>
</p>
</section>

<section id="takeaways" title="总结" kicker="Takeaways">
<h3>再巧妙的机制也次于一套万无一失的推进系统</h3>
<p>
  这个项目显著加深了我对"创意机制"与"底层关卡逻辑"之间平衡的理解。
  我学到的是：即使是最有想象力的玩法——比如抓钩与推块谜题的协同——
  也<b>次于一条不会出错的推进路径</b>；没有合理的钥匙与路径配比，
  一次卡死就足以毁掉整段体验。
</p>

<h3>引导是环境的责任，而不只是 UI 的任务</h3>
<p>
  标记能提供帮助，但真正的直觉来自<b>让关卡几何本身对玩家说话</b>。
  这也是为什么我在最终版里把编号从"标签"重新定位成"视觉锚点"。
</p>

<h3>设计师的职责是编排玩家的情绪节奏</h3>
<p>
  通过从"敌人堆砌"转向有意图的战斗布置，我发现设计师真正在做的事情是
  <b>策划玩家的情绪节奏</b>，让每一个挑战都显得"应得"而不是"恼人"。
</p>
</section>
