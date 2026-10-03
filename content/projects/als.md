---
slug: als
title: ALS 潜入关卡「Infiltration」
subtitle: 攀爬潜入 → 潜行取数据 → 触发警报后限时逃离
summary: 用 Unreal Engine 5 与 ALS 第三人称运动系统做的潜入关卡。三段式节奏（垂直探索 / 潜行 / 限时逃离），核心机制创新是"能量弓按钮链"——玩家必须在掩体后用能量弓按正确顺序射中一串限时按钮。项目最大的收获来自失败：潜行和计时不能混用。
year: "2026"
type: 关卡设计 · 潜入 / 平台跳跃
role: 关卡设计（单人）
team: 个人项目
duration: 2026.03 – 2026.06
engine: Unreal Engine 5.7 + ALS 运动系统
status: 已完成课程作业（PROD387 / PROD323）
tags: ["Unreal Engine 5", "ALS", "潜入", "能量弓", "叙事化引导", "单人项目"]
cover: assets/img/als/cover.jpg
thumb: assets/img/als/cover.thumb.jpg
accent: "#7aa2f7"
order: 2
---

<section id="overview" title="项目概述" kicker="Overview">
<p>
  关卡设定是「Level 5 – Infiltration」：玩家被指控从事间谍活动并被捕，逃出后藏匿起来，
  知道组织里有人陷害自己，但不知道是谁。于是他要潜入自己组织的保密设施，读取电脑里的数据找出真正的间谍，
  然后在被抓住之前逃出去。
</p>
<p>
  这个设定有一个很关键的设计约束：<b>玩家不能伤害守卫</b>——因为那是他自己的组织。
  所有冲突都必须靠潜行和机动来解决，这直接决定了关卡的机制取舍。
</p>

<h3>三段式节奏</h3>
<ol>
  <li><b>垂直探索 / 自由攀爬</b>：从设施外部向上攀爬，寻找潜入点。节奏慢，强调空间感和"这是哪"。</li>
  <li><b>潜行与解谜</b>：在服务器房躲开巡逻守卫的视线，用能量弓远程触发按钮解开锁定的区域。紧张、非战斗。</li>
  <li><b>限时逃离</b>：数据得手、警报响起后，必须在时间压力下穿过移动平台与致命深坑。<b>这是唯一应该出现计时的一段。</b></li>
</ol>

<div class="callout">
  <span class="callout__label">Revise 提示</span>
  <p>
    评审时最希望被注意到的就是<b>这三段之间的节奏转换</b>，以及潜行区里那些"必须躲在低矮掩体后、
    用能量弓按顺序击中一串按钮"的设计。
  </p>
</div>
</section>

<section id="brief" title="关卡简报与约束" kicker="Brief">
<div class="table-scroll">
<table>
  <thead><tr><th>项目</th><th>要求</th></tr></thead>
  <tbody>
    <tr><td>宏观玩法</td><td>必须包含探索、位移（traversal）、潜行、以及限时位移（在时间压力下跑过一段空间）</td></tr>
    <tr><td>必须的节拍</td><td>攀爬探索段 → 潜行段 →（跳过取数据的过场）→ 限时逃离段</td></tr>
    <tr><td>已有机制</td><td>自由攀爬 / 翻越、钥匙与门、潜行、收集物——玩家已经学过，不需要再教</td></tr>
    <tr><td>新机制</td><td>能量弓、能量按钮、能量装置、能量中继——<b>需要做有层次的引入</b></td></tr>
    <tr><td>敌人</td><td>巡逻守卫。玩家不能伤害他们，也不能被发现；因此需要足够密集的检查点，避免被抓后损失太多时间</td></tr>
  </tbody>
</table>
</div>

<h3>新机制的设计空间</h3>
<ul>
  <li><b>能量弓</b>：射出的能量弹不能伤害人或机器人，但可以制造声音引开守卫、射击收集物、触发能量按钮。</li>
  <li><b>能量按钮</b>：开 / 关按钮、<b>限时按钮</b>（击中后开启并随时间衰减）、累积按钮（需要多次命中）、脉冲按钮（周期性通断）。</li>
  <li><b>能量装置与中继</b>：按钮可以把信号中继给其他按钮或装置，用来显隐几何体、开关移动平台。</li>
</ul>

<h3>宏观图与节拍图</h3>
<p>
  正式动工前我先用 Macro Chart 把四段玩法的层级、时长、情绪和所需机制排成一行，
  再据此写 Beat Chart——先定节奏，再定布局。这一步让后面所有"这块地该放什么"的问题都有了参照。
</p>
</section>

<section id="concept" title="概念设计" kicker="Concept">
<h3>一句话提案</h3>
<p>
  一次高风险的潜入体验，把平台跳跃、潜行与解谜缝在一起：玩家要攀爬一座高度戒备设施的外墙，
  潜行穿过重兵把守的服务器房，用能量弓解开"按钮链"谜题来打开封锁区；
  数据到手之后节奏完全翻转，变成在致命深渊上方踩着移动平台的限时跑酷逃亡。
</p>

<h3>主题与地点</h3>
<p>
  主题是「高科技企业数据中心 / 秘密设施」。视觉风格偏写实，但保留高对比度的视觉提示，
  参考方向接近《镜之边缘》与《传送门》。照明是冷调的工业光（冷蓝 + 亮白），
  目的是让<b>发光的能量按钮</b>和<b>橙色的可攀爬平台</b>在环境里一眼可辨。
</p>
<div class="gallery gallery--3">
  <figure class="shot">
    <img src="assets/img/als/mood-1.jpg" alt="情绪板：冷蓝色高技设施内部" loading="lazy" decoding="async">
    <figcaption>情绪板：冷蓝色调的高技设施</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/als/mood-2.jpg" alt="情绪板：压抑的金属走廊" loading="lazy" decoding="async">
    <figcaption>情绪板：压迫感的金属走廊</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/als/mood-3.jpg" alt="情绪板：深色管道空间" loading="lazy" decoding="async">
    <figcaption>情绪板：深色的管道 / 处理区</figcaption>
  </figure>
</div>

<p>
  关卡由三个空间构成：中央带升降机的<b>通风井</b>（初始攀爬与跨越）、
  布满主机、可作为"隐形掩体"的<b>服务器房</b>，以及最后必须靠移动平台跨越的
  <b>深层处理深渊</b>（击杀区）。
</p>

<h3>概念评审反馈</h3>
<blockquote>
  <p>概念一开始偏抽象，看起来像一连串互不相关的平台跳跃挑战或"悬空方块"，而不是一次完整的潜入行动。</p>
  <p>敌人的存在也像是被硬塞进来的障碍，而不是这个世界逻辑的一部分。</p>
</blockquote>
<p>
  <b>我的解法</b>：把抽象方块改造成可识别的道具——低矮掩体排成服务器机架的样子，
  位移段包装成通风管道。这样一来，AI 守卫有了巡逻的合理理由，布局也开始像一个有用途的设施。
  这条反馈后来一直贯穿到最终版。
</p>
</section>

<section id="iteration" title="五个阶段的迭代" kicker="Blockout → Final">
<p>
  这一关经历了 Blockout / Alpha / Beta / Gamma / Final 五个阶段。
  每一轮 playtest 暴露的问题层级都不同 —— 从<b>空间尺度</b>，到<b>节奏</b>，再到<b>难度公平性</b>，
  最后是<b>主题与引导</b>。
</p>

<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/als/blockout-a.jpg" alt="Blockout 阶段的大厅空间" loading="lazy" decoding="async">
    <figcaption>Blockout：优先空间尺度与跳跃距离，而不是美观</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/als/blockout-b.jpg" alt="Blockout 阶段的平台与能量触发器" loading="lazy" decoding="async">
    <figcaption>用能量触发器 + 能量箱测试核心解谜流程是否直观</figcaption>
  </figure>
</div>

<div class="table-scroll">
<table>
  <thead><tr><th>阶段</th><th>Playtest 反馈</th><th>我的修正</th></tr></thead>
  <tbody>
    <tr>
      <td><b>Blockout</b><br>空间尺度与跳跃指标</td>
      <td>在没有贴图的大房间里<b>迷路或走死路</b>，缺少视觉层级；
          部分人<b>误判 ALS 的空中跳跃极限</b>，频繁掉回房间底部</td>
      <td>调整方块位置形成更连续的"楼梯"；重新校准跳跃距离，
          把平台拉近并加入中间安全平台</td>
    </tr>
    <tr>
      <td><b>Alpha</b><br>潜行与限时的冲突</td>
      <td>两名测试者都指出限时过于苛刻。一位明确说
          <b>"给潜行段计时完全抹掉了潜行的感觉"</b>，逼得玩家只能盲目冲刺</td>
      <td>放宽谜题计时。我原本假设"计时 + 潜行 = 更紧迫"，
          这个假设被测试直接否掉</td>
    </tr>
    <tr>
      <td><b>Beta</b><br>难度尖峰与主题不清</td>
      <td>出现了严重的<b>"人为难度"尖峰</b>：红色击杀方块与检查点 6 的守卫
          被评价为"过于惩罚，而不是公平的挑战"；
          四人中三人觉得环境太抽象，说不清这是什么设施</td>
      <td>放宽计时；但为增强逃离段风险加入的击杀方块与守卫，
          反而制造了不公平的难度 —— 这条在下一阶段继续处理</td>
    </tr>
    <tr>
      <td><b>Gamma</b><br>修引擎层面的摩擦</td>
      <td>所有测试者的共同意见：关卡仍像"一个洞"或"一堆橙色方块"，
          不像真实的潜入地点；AI 守卫因此显得随意
          （环境看起来不值得守卫）</td>
      <td>纯技术修复：把可攀爬方块从贴墙位置拉开（否则翻越动画不触发）、
          统一 mantle 高度、<b>缩小蹲伏区击杀区的碰撞盒</b>修掉不公平死亡</td>
    </tr>
    <tr>
      <td><b>Final</b><br>用环境本身做引导</td>
      <td>线性引导与谜题逻辑受到肯定；"用能量弓按顺序击打一串限时按钮"
          被评价为对机制的聪明用法</td>
      <td>保留按钮链结构，但把它整合进重做的环境：用蓝色瓷砖与工业混凝土
          分区，并在墙面加入叙事化 AR 文字承担引导职能</td>
    </tr>
  </tbody>
</table>
</div>

<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/als/final-a.jpg" alt="Final 阶段：蓝色瓷砖与工业混凝土分区" loading="lazy" decoding="async">
    <figcaption>用蓝色瓷砖与工业混凝土分开不同玩法区域</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/als/final-b.jpg" alt="Final 阶段墙面的 AR 警告文字" loading="lazy" decoding="async">
    <figcaption>叙事化 AR 文字："Warning: Automated security on patrol"</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/als/final-c.jpg" alt="Final 阶段墙面的提示文字" loading="lazy" decoding="async">
    <figcaption>"You need to find both vents and hack it"</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/als/final-d.jpg" alt="Final 阶段的击杀区与警示文字" loading="lazy" decoding="async">
    <figcaption>"INCINERATOR ACTIVE. HAZARD ZONE BELOW"</figcaption>
  </figure>
</div>
</section>

<section id="takeaways" title="总结与反思" kicker="Takeaways">
<h3>潜行和计时不能混用</h3>
<p>
  早期版本我给潜行段加了计时，以为会更刺激。结果只是让测试者恐慌、盲目冲刺、然后烦躁。
  我意识到<b>潜行需要给玩家时间和安全空间去观察</b>，而限时逃离应该是独立的另一段——
  这两者的情绪需求是相反的，不能叠在同一段玩法里。
</p>

<h3>用环境引导玩家</h3>
<p>
  当关卡还是"一堆橙色方块"的时候，玩家既迷路，也不理解 AI 守卫为什么会在这里。
  把 "Warning"、"Incinerator Active" 这类文字直接写在墙上，是我这个项目最重要的收获：
  它在不打断沉浸的前提下，自然地把玩家推向下一步。
</p>

<h3>关卡设计不只是指标精准的跳跃</h3>
<p>
  整个项目最大的结论是：关卡设计不只是"把跳跃距离调准"，而是
  <b>把这些跳跃放进一个叙事上说得通的空间里</b>。测试、失败、再修正的循环过程本身，
  比任何一次单独的成功修改都更有价值。
</p>

<div class="callout">
  <span class="callout__label">评级说明</span>
  <p>
    这一关经过了大量基于 playtest 的迭代。早期版本被批评"只是橙色方块"、跳跃距离令人烦躁；
    最终版在"场所感"上投入了很多，把方块重构为可信的高科技数据设施，并重新校准了跳跃指标，
    让难度<b>有挑战但公平</b>。
  </p>
</div>
</section>
