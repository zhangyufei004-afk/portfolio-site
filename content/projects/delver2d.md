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

<p>
  这一关经历了 Blockout / Alpha / Beta / Final 四个阶段，
  每一轮 playtest 都改变了"问题在哪"的判断。
</p>

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

<div class="table-scroll">
<table>
  <thead><tr><th>阶段</th><th>Playtest 反馈</th><th>我的修正</th></tr></thead>
  <tbody>
    <tr>
      <td><b>Blockout</b></td>
      <td>抓钩与地形解谜被评价为有创意，但存在严重的<b>导航问题</b>：
          玩家常走到关卡末端才发现漏了第三间房的钥匙，只能把整张地图再走一遍；
          错放的传送器与"用抓钩穿过方块"这类非直觉解法放大了迷路</td>
      <td>把体验从<b>重战斗</b>转向<b>环境位移与空间解谜</b>，
          并围绕"抓钩 + 推块"的协同重建关卡</td>
    </tr>
    <tr>
      <td><b>Alpha</b></td>
      <td>推进变得"非常清晰"，抓钩触发压力板等用法获得好评；
          但仍觉得敌人太多，明确指出 <b>Boss 房像一个"敌人堆砌场"</b></td>
      <td>把钥匙房从第三间房挪到<b>紧邻抓钩获取点</b>，解决过度回头路；
          全图加入<b>数字编号</b>辅助导航</td>
    </tr>
    <tr>
      <td><b>Beta</b></td>
      <td>暴露两个更严重的问题：一是<b>很高的卡死风险</b>——
          测试者被困在<b>有锁门但没有钥匙</b>的房间里且无法回头；
          二是数字标记<b>并不直观</b>。部分测试者因此没能完整通关</td>
      <td>重排战斗与解谜配比：第二间房移除两个刷怪点改成<b>推块 + 压力杆</b>；
          把普通门替换成<b>清光敌人才开锁</b>的房间锁</td>
    </tr>
    <tr>
      <td><b>Final</b></td>
      <td>—（针对 Beta 暴露的卡死风险做主动审查）</td>
      <td><b>把"逻辑安全"放在复杂度之上</b>：完整审查所有钥匙与门的位置，
          重构返回路径，确保玩家就算漏掉道具也永远不会被困住；
          把编号升级为澄清解谜顺序的<b>视觉锚点</b>；
          用有意图的遭遇替换杂乱刷怪</td>
    </tr>
  </tbody>
</table>
</div>

<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/delver2d/beta-before.jpg" alt="Beta 之前的关卡布局" loading="lazy" decoding="async">
    <figcaption>Beta 之前</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/delver2d/beta-after.jpg" alt="Beta 之后的关卡布局" loading="lazy" decoding="async">
    <figcaption>Beta 之后：削减敌人，用推块与压力杆组合替代刷怪</figcaption>
  </figure>
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
  这个过程让我明白：<b>保护玩家的心流，和挑战玩家的心流同样重要。</b>
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
