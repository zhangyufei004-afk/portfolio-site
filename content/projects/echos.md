---
slug: echos
title: ECHOES
subtitle: 在漆黑迷宫里，被一只只对光和声音有反应的怪物追杀
summary: 单人开发的潜行恐怖原型。核心是一套 Patrol / Suspicious / Chase / Attack 有限状态机，配合 Unity NavMesh 寻路、听觉与视觉感知，以及一个让玩家能主动切断追踪的躲藏机制。三轮 playtest 迭代把它从"不公平的逃跑模拟器"推成了一款战术潜行体验。
year: "2026"
type: 潜行恐怖 · AI 系统
role: 单人开发（设计 / 程序）
team: 个人项目
duration: 2026.03 – 2026.06
engine: Unity（C#）+ Mixamo 动画
status: 已完成的课程作业（PROD323 Assignment 2）
tags: ["Unity", "有限状态机", "NavMesh", "AI 感知", "恐怖", "单人项目"]
cover: assets/img/echos/cover.jpg
thumb: assets/img/echos/cover.thumb.jpg
accent: "#5ee0d0"
order: 1
---

<section id="overview" title="项目概述" kicker="Overview">
<p>
  ECHOES 是一个潜行恐怖原型。玩家身处一座几乎没有光照的迷宫，逐步收集 3 个符文（Runes）打开出口；
  与此同时，一只怪物在迷宫里巡逻。它看不见整个地图，只能靠<b>视线</b>和<b>声音</b>感知玩家，
  于是"黑暗"既是玩家的掩护，也是它最好的猎场。
</p>

<p>
  项目的约束条件很明确：单人、4 周、课程作业。所以我在立项阶段就把范围锁死在
  <b>"高张力的 AI 感官机制与状态转移"</b>上，刻意不碰复杂美术、不碰复杂 UI、不做程序化生成、
  不做网络或 LLM 相关的任何东西——所有会让"这一周做不完"的东西都被砍掉了。
</p>

<h3>玩家循环</h3>
<ol>
  <li><b>探索</b>：在黑暗中移动，寻找符文与出口。</li>
  <li><b>感知风险</b>：通过小地图判断怪物的方位，避开它的巡逻路线。</li>
  <li><b>被察觉</b>：一旦产生噪声或进入视线，怪物转入 Suspicious，前往最后已知位置搜索。</li>
  <li><b>应对</b>：跑（会被追上）、躲（按键隐藏，切断视听痕迹）或赌它搜索失败。</li>
</ol>

<div class="callout">
  <span class="callout__label">一句话</span>
  <p>我想做的不是"跑得比怪物快"，而是"在信息不足的情况下做对判断"。</p>
</div>
</section>

<section id="concept" title="设计概念筛选" kicker="Week 8 · Crazy 8">
<p>
  立项时我用 Crazy 8 的方式一次性铺开 8 个方向，然后逐个以"AI 深度"和"4 周单人可实现性"两个轴筛掉。
  下面是被否掉的方向和具体理由——这张表其实是我后来所有设计决策的边界条件。
</p>

<div class="table-scroll">
<table>
  <thead>
    <tr><th>构想</th><th>概念</th><th>否掉的原因</th></tr>
  </thead>
  <tbody>
    <tr><td>僵尸 FPS 生存</td><td>在固定场地抵御一波波僵尸</td><td>AI 行为只有直线寻路，缺乏这门课真正想要的深度</td></tr>
    <tr><td>战术社交潜行</td><td>潜入派对并刺杀目标（Hitman 风格）</td><td>动画与 FSM 规模过大——要管理数十个 NPC 的恐慌 / 搜索 / 警戒状态，单人 4 周做不完</td></tr>
    <tr><td>RTS 资源管理</td><td>控制多个单位采集资源并战斗</td><td>群体逻辑与局部避障的复杂度会直接导致范围失控</td></tr>
    <tr><td>AI 同伴解谜</td><td>聪明的 AI 宠物帮玩家解决环境谜题</td><td>友好 AI 一旦卡住或犯错，玩家体验会直接崩掉，风险太高</td></tr>
    <tr><td>群体驱赶模拟</td><td>把数百个 boid 单位赶进指定区域</td><td>技术上可行，但缺少有说服力的玩法循环，更像技术演示</td></tr>
    <tr><td>LLM 侦探审讯</td><td>调用 LLM API 审问嫌疑人并破案</td><td>网络延迟不可控 + 输出非确定性，会让 playtest 和评分都不可靠</td></tr>
    <tr><td>PCG Roguelike 地牢</td><td>程序化生成地图与随机敌人</td><td>时间会耗在关卡生成算法上，而不是打磨核心的 Agent AI 逻辑</td></tr>
    <tr><td><b>感官潜行迷宫</b>（选中）</td><td>在漆黑迷宫中躲避对光 / 声有反应的捕食者</td><td><b>范围刚好</b>：完全聚焦于高张力的 AI 感官机制与状态转移，不需要被复杂美术或 UI 拖累</td></tr>
  </tbody>
</table>
</div>

<p>
  回过头看，这次筛选最有价值的部分不是选中了什么，而是<b>把"不做什么"写清楚了</b>。
  后面每一次想加功能的时候，我都先回来对一下这张表。
</p>
</section>

<section id="references" title="参考作品分析" kicker="Week 9 · Reference Analysis">
<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/echos/ref-pacman.jpg" alt="Pac-Man 街机封面" loading="lazy" decoding="async">
    <figcaption>Pac-Man —— 确定性状态循环的教科书</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/echos/ref-amnesia.jpg" alt="Amnesia: The Dark Descent 封面" loading="lazy" decoding="async">
    <figcaption>Amnesia: The Dark Descent —— 把光变成生存资源</figcaption>
  </figure>
</div>

<h3>Amnesia：光作为生存资源</h3>
<p>
  Amnesia 最关键的启发是"脆弱性来自资源管理"。我把这一点转译成了
  <b>光照强度直接参与 AI 的侦测阈值</b>：玩家手里的光既能让自己看清路，也会把自己暴露出去。
  于是"要不要开灯"变成一个每次都要重新算的决策，而不是一个可以固定下来的习惯。
</p>

<h3>Pac-Man：确定性的状态循环</h3>
<p>
  Pac-Man 的幽灵 AI 一点也不复杂，但它的 Scatter / Chase 循环制造了非常稳定的压迫节奏。
  我把这个思路直接搬进了 FSM：怪物的行为<b>可预测到能被学会</b>，但<b>持续到足以让人紧张</b>。
  恐怖感不来自随机性，而来自"我知道它接下来会做什么，但我不确定自己来不来得及"。
</p>
</section>

<section id="fsm" title="AI 设计：有限状态机" kicker="核心系统">
<p>
  AI 的骨架是一个四状态 FSM。每个状态都有明确的进入条件、行为响应和退出条件，
  这样"怪物为什么这样动"永远可以追溯到一条具体规则，而不是"感觉它在追我"。
</p>

<div class="table-scroll">
<table>
  <thead>
    <tr><th>状态</th><th>触发条件</th><th>行为响应</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Patrol</b><br><span class="dim">巡逻</span></td>
      <td>玩家未被侦测到</td>
      <td>用 NavMesh 在一个随机化的路径点列表中迭代移动，维持对整个迷宫的覆盖</td>
    </tr>
    <tr>
      <td><b>Suspicious</b><br><span class="dim">警觉</span></td>
      <td>听到噪声，或看到闪烁的灯光</td>
      <td>停止巡逻，移动到 LastKnownPosition，<b>原地停留 5 秒"搜索"</b>该区域，然后重置回 Patrol</td>
    </tr>
    <tr>
      <td><b>Chase</b><br><span class="dim">追击</span></td>
      <td>确认直接视线（LOS）</td>
      <td>高速追击模式，用 NavMesh 计算到玩家实时 Transform 的最短路径</td>
    </tr>
    <tr>
      <td><b>Attack</b><br><span class="dim">攻击</span></td>
      <td>玩家进入攻击距离</td>
      <td>停止移动，锁定朝向面对玩家，播放攻击动画，随后触发 Death UI</td>
    </tr>
  </tbody>
</table>
</div>

<figure class="shot">
  <img src="assets/img/echos/architecture.jpg" alt="系统架构图：玩家输入、AI 感知系统与 FSM 之间的数据流" loading="lazy" decoding="async">
  <figcaption>系统架构草图：玩家输入 → 感知系统（视觉 / 听觉 / 光照）→ FSM → 怪物行为，并由 Rune 系统与 Game Manager 决定胜负条件。</figcaption>
</figure>

<h3>为什么选 FSM 而不是行为树 / 效用 AI</h3>
<p>
  在 4 周的单人范围里，FSM 的价值是<b>可调试</b>：任何一次"怪物行为看起来不对"，我都能定位到具体是哪个转移条件写错了，
  而不是在一棵行为树里猜优先级。事后复盘时我认为这是这个项目做对的最关键决定——
  状态分离让 AI 既"可学到"，又"持续可怕"。
</p>
</section>

<section id="navmesh" title="寻路与感知实现" kicker="技术实现">
<p>
  寻路用的是 Unity 的 NavMesh 系统，这样迷宫里的复杂转角不会让 AI 卡在几何边缘。
  路径烘焙、Agent 参数、感知范围这些细节恰恰是后面两轮迭代的主要战场。
</p>

<figure class="shot">
  <img src="assets/img/echos/navmesh-bake.jpg" alt="Unity 导航窗口中的 NavMesh 烘焙结果" loading="lazy" decoding="async">
  <figcaption>在 Unity Navigation 窗口中烘焙迷宫的可通行区域。</figcaption>
</figure>

<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/echos/blockout-level.jpg" alt="迷宫 blockout 与玩家视角" loading="lazy" decoding="async">
    <figcaption>Blockout：刻意做成窄走廊 + 盲转角，强制近距离遭遇。</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/echos/ai-placeholder.jpg" alt="用胶囊体占位的 AI 与符文计数 UI" loading="lazy" decoding="async">
    <figcaption>AI 从代码到角色：FSM 先在胶囊体占位上跑通端到端，再换成模型。</figcaption>
  </figure>
</div>

<h3>感知的两条通道</h3>
<ul>
  <li><b>视觉</b>：由视线判定 + 光照强度共同决定——站在亮处更容易被发现。</li>
  <li><b>听觉</b>：玩家的移动产生噪声事件，噪声半径决定怪物能否听到。</li>
</ul>
<p>
  两条通道的意义在于：它们给玩家提供了<b>两种不同的隐藏策略</b>（避光 vs. 保持安静），
  而不是一个"离远点就安全"的单一维度。
</p>
</section>

<section id="iteration" title="三轮迭代" kicker="Playtest 驱动的修改">
<p>
  这个项目真正的设计工作几乎都发生在 playtest 之后。下面三次迭代各自解决了一个具体问题，
  而且每一次都改变的是<b>系统</b>，不只是数值。
</p>

<h3>迭代 1 · 不公平的巡逻 → 躲藏机制</h3>
<figure class="shot">
  <img src="assets/img/echos/monster-model.jpg" alt="怪物模型在走廊中" loading="lazy" decoding="async">
  <figcaption>怪物开始巡逻后，窄走廊里玩家没有任何反制手段。</figcaption>
</figure>
<p>
  <b>观察</b>：玩家反馈很挫败——迷宫走廊太窄，怪物一旦开始巡逻，玩家既无法绕开，也无法切断视线。
</p>
<p>
  <b>解法</b>：加入可交互的躲藏机制。玩家按 <code>E</code> 躲进柜子，期间<b>临时关闭自身的视觉与听觉痕迹</b>。
</p>
<figure class="shot">
  <img src="assets/img/echos/hiding-cabinet.jpg" alt="用于躲藏的古董柜模型" loading="lazy" decoding="async">
  <figcaption>躲藏点：古董柜（Antique Cabinet）。</figcaption>
</figure>
<p>
  这个改动把游戏从"挫败的跑步模拟器"变成了有战术层的潜行——玩家第一次拥有了主动切断追踪的能力，
  难度感也随之从"不公平"变成"公平但紧张"。
</p>

<h3>迭代 2 · 怪物穿墙 → 重新烘焙 NavMesh</h3>
<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/echos/navmesh-agent-radius-a.jpg" alt="调整 Agent Radius 前的追击表现" loading="lazy" decoding="async">
    <figcaption>调整前：追击转弯时上半身和手臂穿进墙体。</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/echos/navmesh-agent-radius-b.jpg" alt="调整 Agent Radius 后的追击表现" loading="lazy" decoding="async">
    <figcaption>调整后：AI 与障碍物保持合理距离。</figcaption>
  </figure>
</div>
<p>
  <b>观察</b>：怪物在拐角追击玩家时，上半身与手臂频繁穿进水泥墙，直接破坏沉浸感。
</p>
<p>
  <b>根因</b>：不是动画问题，而是 <b>AI 物理模型尺寸与 Unity NavMesh 设置不匹配</b>——烘焙出的路径离墙太近。
</p>
<p>
  <b>修复</b>：打开 Navigation 窗口，<b>增大 Agent Radius 并重新烘焙</b>，强制 AI 与障碍物保持真实距离。
</p>
<p class="dim">
  这条经验我后来反复用到：当"表现层看起来很怪"时，先怀疑系统层的数据，而不是先去改动画。
</p>

<h3>迭代 3 · 迷路与贴脸惊吓 → 小地图雷达</h3>
<figure class="shot">
  <img src="assets/img/echos/cover.jpg" alt="小地图雷达与迷宫内的光照" loading="lazy" decoding="async">
  <figcaption>高对比度小地图雷达：既解决导航，也让玩家能预判盲转角后的怪物。</figcaption>
</figure>
<p>
  <b>问题</b>：第二轮 playtest 暴露出两个问题——玩家在黑暗迷宫里完全找不到出口；
  窄转角导致"贴脸"惊吓，玩家直接撞进怪物怀里，感觉是被惩罚而不是被吓到。
</p>
<p>
  <b>解法</b>：实现高对比度小地图雷达。技术上的做法是
  <b>把迷宫几何复制到一个自定义的 <code>MinimapOnly</code> 层，用 Unlit shader 渲染，从而绕过全局雾</b>。
</p>
<p>
  设计上这个改动同时解决了两件事：导航不再是纯靠记忆的折磨，玩家也第一次拥有了
  <b>预判盲转角威胁的战术工具</b>。生存体验因此变得"公平且有策略"。
</p>

<h3>胜负循环</h3>
<p>
  收集到 3 个符文并抵达出口即逃脱成功；被怪物追上则触发死亡界面。这两端构成了整段紧张感的收束点。
</p>
<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/echos/win-screen.jpg" alt="逃脱成功界面：Runes 3/3 与 You Are Escaped!" loading="lazy" decoding="async">
    <figcaption>逃脱成功：符文 3/3，<code>You Are Escaped!</code></figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/echos/death-screen.jpg" alt="死亡界面：You Died!" loading="lazy" decoding="async">
    <figcaption>被追上的结果：死亡界面，怪物攻击动画结束后触发</figcaption>
  </figure>
</div>
</section>

<section id="postmortem" title="复盘" kicker="Post-Mortem">
<h3>做得好的</h3>
<ul>
  <li>
    <b>FSM 架构</b>：对这个范围来说是最合适的选择。Patrol / Suspicious / Chase 的清晰分离，
    让 AI 可预测到能被学会，又持续到足以让人害怕。
  </li>
  <li>
    <b>躲藏机制</b>：允许玩家切断视线这一件事，就把游戏从"挫败的跑步模拟器"
    彻底改造成了战术潜行体验。
  </li>
</ul>

<h3>失败与摩擦</h3>
<ul>
  <li>
    <b>光照与可玩性的平衡</b>：把恐怖游戏做得够黑才有氛围，但又要够亮才玩得下去——
    这件事比我预想的难得多。最初依赖全局雾，结果是<b>玩家和 UI 摄像机一起被糊住了</b>。
  </li>
  <li>
    小地图的解法（复制几何 + Unlit + 独立层）虽然有效，但说明我在<b>渲染管线层面缺少前期规划</b>：
    如果一开始就把"哪些东西需要无视雾"想清楚，可以省掉这轮返工。
  </li>
</ul>

<div class="callout">
  <span class="callout__label">如果再做一次</span>
  <p>
    我会在 blockout 阶段就同时标出"光照强度分区"和"躲藏点分布"，
    让恐怖氛围与可玩性从第一版就一起被验证，而不是等 playtest 发现玩不下去之后再回头补。
  </p>
</div>
</section>

<section id="credits" title="素材与参考" kicker="Credits">
<ul>
  <li><b>参考作品</b>：
    <a href="https://en.wikipedia.org/wiki/Pac-Man" target="_blank" rel="noopener noreferrer">Pac-Man</a> ·
    <a href="https://en.wikipedia.org/wiki/Amnesia:_The_Dark_Descent" target="_blank" rel="noopener noreferrer">Amnesia: The Dark Descent</a>
  </li>
  <li><b>怪物 3D 模型与动画</b>：Adobe Mixamo（<a href="https://www.mixamo.com/" target="_blank" rel="noopener noreferrer">mixamo.com</a>），包含 Walk / Sprint / Attack 三个核心 AI 行为动画</li>
  <li><b>古董柜模型</b>：Unity Asset Store — Antique Cabinet</li>
  <li><b>环境 / 迷宫贴图</b>：Unity Asset Store — PBR Hospital Horror Pack (Free)</li>
  <li><b>音效</b>：Pixabay — 恐龙脚步与沉重角色行走音效</li>
</ul>
<p class="dim">
  除上述第三方素材外，关卡 blockout、AI 系统、FSM 逻辑、躲藏机制与小地图雷达均为本人实现。
</p>
</section>
