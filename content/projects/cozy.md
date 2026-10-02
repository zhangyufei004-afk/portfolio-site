---
slug: cozy
title: Cozy Fishing
subtitle: 六人团队、Scrum 与 Git Flow 下的休闲钓鱼游戏
summary: PC / 主机的休闲风格钓鱼游戏：探索岛屿、接任务、在多种钓鱼小游戏里磨练技巧。我负责商店、鱼类图鉴、任务、主菜单 / 暂停 / 设置等系统的界面逻辑与交互原型——信息架构、交互流程与功能实现由我完成，组员在此基础上做视觉优化。脚本刻意写成可复用、可扩展的形式，让设计团队不用改核心系统就能加内容。
year: "2025"
type: 休闲游戏 · 团队项目
role: 界面系统设计与实现（商店 / 图鉴 / 任务 / 设置）
team: 6 人团队（In2Games 行业合作课程）
duration: 2025.07 – 2025.10
engine: Unity + Maya / Blender
status: 已完成课业，产出可玩 Demo（PROD322 校企合作项目）
tags: ["Unity", "界面系统", "ScriptableObject", "数据驱动", "Scrum", "Git Flow", "6 人团队"]
cover: assets/img/cozy/cover.jpg
thumb: assets/img/cozy/cover.thumb.jpg
accent: "#6fc7e8"
order: 7
---

<section id="overview" title="项目概述" kicker="Overview">
<p>
  Cozy Fishing 是一款 PC / 主机的休闲风格钓鱼游戏。玩家可以探索一座岛屿、接取任务，
  并通过几种不同主题的钓鱼小游戏磨练技巧。整体调性温馨，同时强调环保与保育主题。
</p>
<div class="table-scroll">
<table>
  <thead><tr><th>成员</th><th>专业</th><th>主要职责</th></tr></thead>
  <tbody>
    <tr><td>Ben</td><td>动画</td><td>建模与动画——最终版本中所有动画以及玩家模型都出自他</td></tr>
    <tr><td>Brayden</td><td>AIGD</td><td>程序与玩法设计——最终版本里大部分小游戏由他设计</td></tr>
    <tr><td>Liz</td><td>AIGD</td><td>技术美术、建模、2D 美术——最终版本的全部关卡设计、shader，以及大部分 2D 与部分 3D 资产</td></tr>
    <tr><td>Madi</td><td>AIGD + 软件工程</td><td>Git 管理与程序——通过代码审查流程让代码库与 git 流程保持干净</td></tr>
    <tr><td>Tobey</td><td>AIGD</td><td>程序与音效设计——最终版本中所有音效都由他设计与实现</td></tr>
    <tr><td><b>Yufei</b></td><td>AIGD</td><td><b>界面系统的设计与实现——商店、图鉴、任务、设置等系统的信息架构、交互流程与功能原型</b></td></tr>
  </tbody>
</table>
</div>
</section>

<section id="role" title="我的工作" kicker="My Contribution">
<p>
  我负责的是<b>界面系统的逻辑层</b>：商店、图鉴、任务与设置这些系统的
  <b>信息架构、交互流程与功能原型</b>都由我设计与实现——做出来的是<b>带实际功能、
  可直接游玩</b>的版本，也就是最终呈现的形态。组员在此基础上做视觉优化
  （重新布局、把 UI 素材替换为她自己绘制的 sprite）。
</p>
<p>
  此外我把这些系统的脚本写成<b>数据驱动、可扩展</b>的形式，
  让设计团队不必改动核心代码就能加新内容——这也是为什么同一套图鉴界面
  既能装下鱼类，也能装下钓上来的杂物。
</p>

<h3>我实现的系统</h3>
<ul>
  <li>
    <b>图鉴 / 记录系统（Fish Log）</b>：记录玩家的每一次收获，包含名称、重量、
    长度、发现时段与地点。这套结构是<b>数据驱动</b>的——同一套界面既承载鱼类，
    也承载钓上来的杂物（例如 0.38 kg 的罐头），<b>新增一类收集品不需要改界面</b>。
    条目在每次成功上钩后动态更新，玩家会主动去凑齐尚未解锁的剪影。
  </li>
  <li>
    <b>任务系统（Quests）</b>：承接任务、展示分阶段目标与阶段奖励。
    与图鉴、商店串成"接任务 → 探索与钓获 → 交付领奖 → 买更好鱼饵"的循环。
  </li>
  <li>
    <b>背包与物品管理</b>：物品的存储与检索，包括槽位处理、界面更新，
    以及与其他玩法系统对接的标记（tagging）逻辑。
  </li>
  <li>
    <b>商店（Shop）</b>：买卖两侧布局把渔获、货币与鱼饵连接起来，构成经济循环。
    每种鱼饵对应特定鱼种，所以"买什么饵"本身就是玩家的策略选择，
    而不只是数值升级。
  </li>
  <li>
    <b>钓鱼小游戏原型</b>：设计 <b>DDR 式</b>钓鱼小游戏（以节奏输入承载轻量化操作），完成原型后交由组员继续精细打磨。
  </li>
  <li>
    <b>主菜单</b>：开始 / 设置 / 退出，并确保场景切换顺畅。
  </li>
  <li>
    <b>暂停菜单</b>：继续 / 退出 / 设置集成，并接入 <b>Unity 新的 Input System</b>。
  </li>
  <li>
    <b>设置 UI</b>：为玩法与音频提供可配置面板，并用脚本支持基于场景的切换。
  </li>
  <li>
    <b>角色自定义</b>：同时提供<b>滑条式 RGB 控制</b>与<b>预设颜色按钮</b>，用于调整头发与帽子的颜色。
    这个系统直接把改动应用到材质上，并支持实时预览。
  </li>
</ul>

<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/cozy/ui-shop.jpg" alt="商店界面：左侧 Sell 出售渔获，右侧 Buy 购买鱼饵，顶部显示持有货币" loading="lazy" decoding="async">
    <figcaption><b>商店</b>：Sell 侧卖出渔获换货币，Buy 侧购买鱼饵。每种鱼饵对应特定鱼种，「买什么饵」本身就是策略选择</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/cozy/ui-quests.jpg" alt="任务书界面：左侧任务列表，右侧分阶段目标与奖励" loading="lazy" decoding="async">
    <figcaption><b>任务书</b>：承接任务、查看分阶段目标与奖励，与图鉴和商店串成完整循环</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/cozy/ui-fishlog-caught.jpg" alt="图鉴中已捕获的条目：Goblin Fish 1.02kg 的记录页" loading="lazy" decoding="async">
    <figcaption><b>图鉴（已解锁）</b>：每次收获都记录名称、重量、时段与地点</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/cozy/ui-log-tincan.jpg" alt="图鉴中记录钓到的罐头：Tin Can 0.38kg，发现于 Morning / Ocean" loading="lazy" decoding="async">
    <figcaption><b>同一套结构装杂物</b>：钓上来的罐头走完全相同的记录结构 —— 这是界面数据驱动的直接证据</figcaption>
  </figure>
</div>
<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/cozy/ui-customise.jpg" alt="角色自定义界面：头发与帽子的 RGB 滑条与预设色板" loading="lazy" decoding="async">
    <figcaption><b>角色自定义</b>：滑条式 RGB 控制 + 预设色板，实时预览并直接应用到材质</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/cozy/shot-b.jpg" alt="Cozy Fishing 的主菜单" loading="lazy" decoding="async">
    <figcaption><b>主菜单</b>：开始 / 设置 / 荣誉榜 / 退出</figcaption>
  </figure>
</div>
<figure class="shot">
  <img src="assets/img/cozy/shot-c.jpg" alt="Cozy Fishing 的设置界面" loading="lazy" decoding="async">
  <figcaption>设置 UI：分辨率与显示模式等可配置项</figcaption>
</figure>

<div class="links">
  <a class="btn" href="https://www.bilibili.com/video/BV19z8t65ED8/" target="_blank" rel="noopener noreferrer">
    演示视频（Bilibili） <span class="btn__hint">↗ 站外页面</span>
  </a>
  <a class="btn" href="https://github.com/zhangyufei004-afk/Cozy-Fishing" target="_blank" rel="noopener noreferrer">
    GitHub 仓库 <span class="btn__hint">↗ 站外页面</span>
  </a>
</div>
</section>

<section id="process" title="流程与协作" kicker="Process">
<div class="grid grid--2">
  <div class="pillar">
    <h3>工具</h3>
    <ul>
      <li>Discord：按正在开发的机制分频道，并用于组织会议</li>
      <li>Trello：按 sprint 分区，任务<b>自分配</b>，由全队共同维护而不是交给某一个人</li>
      <li>EngGit（坎特伯雷大学的 GitLab）：行业标准的 <b>Git Flow</b></li>
      <li>引擎 Unity；建模以 Maya 为主、Blender 处理较小的模型</li>
    </ul>
  </div>
  <div class="pillar">
    <h3>流程</h3>
    <ul>
      <li><b>Scrum</b>：feature 拆成 story，story 再拆成任务，以两周为一个 sprint</li>
      <li>每个 sprint 首周二 sprint planning；周五与周二 stand-up；最后周五 sprint review（对客户）与 retrospective</li>
      <li>所有新功能在独立分支开发，完成后提 merge request 进 develop，由 Git 负责人 review 后合并</li>
      <li>sprint 末把 develop 合并进 main，代表最新可玩版本</li>
      <li>统一<b>代码风格文档</b>：变量命名、类与方法文档、方法排序顺序</li>
    </ul>
  </div>
</div>
</section>

<section id="retro" title="团队复盘中的关键问题" kicker="Retrospective">
<p>
  这份报告里最有价值的部分是团队对流程问题的复盘。我把自己认为最值得记住的几条整理在这里。
</p>

<h3>沟通不畅</h3>
<p>
  影响范围从"一个变量赋错了值"到更严重的问题。其中一个典型案例是：
  两个开发者之间沟通不到位，一个原本为私有的变量在另一个开发者手上需要变成公开，
  结果导致<b>用反射去修改私有变量</b>这种恶劣写法。
  问题在代码审查中被发现并记录，随后分别与两位开发者沟通、要求他们互相协调，
  并在 sprint retrospective 上再次作为问题提出，提醒所有人：
  如果需要改动代码库的其它部分，是可以改的，但请先和写那段代码的人沟通。
</p>

<h3>最后一刻才提交合并请求</h3>
<p>
  每星期五中午要出一版可运行的游戏，于是所有功能也必须在周五中午前完成。
  但可运行版本来自 develop 分支，当所有 merge request 都堆在周五早上，
  合并与审查就变成了灾难：审查时间不足，本已做好的功能被迫延期，
  Git 维护者的工作量也剧增（每次 develop 变动，她都要把所有待合并分支更新一遍）。
</p>
<p>
  <b>最终解法</b>：在最后一个 sprint 把 merge request 的截止时间提前到周二上午，
  给维护者留出合并与审查的时间，也给发现问题后的修改留出空间。
</p>

<h3>提交太少（Lack of commits）</h3>
<p>
  团队内 Git 经验差距很大。Git 的常规建议是"频繁提交、经常推送"，
  有团队项目经验的人照做了，经验少的人没有。提交太少听起来不是大问题，
  但在处理 merge request 时非常致命：<b>一旦需要修改，可能整个 sprint 的工作都会被抹掉</b>。
  虽然开会提醒过，但一个星期后就会恢复原样。
  <b>结论</b>：未来应该坐下来手把手带这些开发者走一遍流程。
</p>

<h3>美术资产优先级错位</h3>
<p>
  初期只有代码功能被排优先级，美术资产没有。结果是<b>做什么模型由建模师自己决定</b>，
  于是先做了更容易但非必要的模型，而一些更关键的元素直到最终版仍是占位资产。
  未来应该在开发早期就把美术资产的优先级定下来。
</p>

<h3>贡献不均</h3>
<p>
  这是贯穿整个项目的问题。多数成员贡献相当，但有成员明显偏少，
  等于团队以更少的人在工作。原本在初期规划中属于范围内的功能因此被砍成 stretch goal。
  团队尝试过小截止日期、个人截止日期、人员轮换，都没有真正解决。
  未来如果再次出现，<b>或许需要更严格的管理风格</b>来盯住贡献偏少的人。
</p>

<h3>客户参与度</h3>
<p>
  客户（In2Games）在第一学期参与度很低，但至少会开会讨论进展与改进建议。
  第二学期情况完全改变——客户<b>直接停止与团队沟通</b>，
  连邀请他们参加的课堂汇报也不出席。团队只能自行决定设计与方向。
  这对团队不是致命问题，但对客户是：客户对游戏有预期，
  而团队因为无法联系到客户，永远无法完全满足这些预期。
  最终成品符合<b>团队对简报的理解</b>，但不一定符合客户的。
</p>

<h3>单点故障</h3>
<p>
  这可能是项目中最严重的单点问题：团队里只有一名动画师、一名技术美术，
  以及一名能可靠地合并与 review 代码的人。其中任何一个人生病或离开，项目就会停摆。
  事实也确实发生过：Git 维护者生病时 merge request 被搁置，
  动画师生病时动画一段时间没有任何进展。
</p>
<ul>
  <li><b>Git 单点可以解决</b>：教会其他人合并技巧与代码审查礼仪，让 develop 可以由多人合并。</li>
  <li><b>动画与技术美术很难解决</b>：动画软件需要数年积累，无法靠内部培训补上；只能靠<b>在 sprint 规划时把病假因素算进去</b>，
    让生病的人能专注恢复。</li>
</ul>

<h3>技术问题</h3>
<ul>
  <li>
    <b>合并</b>：所有人都在主场景里工作，导致 inspector 变量频繁被覆盖，越到后期越痛苦。
    另一个问题是部分成员对合并缺乏信心，做完的分支干脆不合并，
    让 Git 负责人除了审查代码还要手工合并。这个问题在第四学期有改善。
    回头看在<b>独立场景里工作</b>会更好。
  </li>
  <li>
    <b>Maya 到 Unity 的动画导出</b>：角色模型的绑定与动画转换出了问题，
    而且很难定位错在哪里，导致动画师有<b>数周</b>无法为主角做动画。
    最终根因是<b>从 Maya 导入 Unity 时的缩放（scaling）错误</b>。
    动画师从中学会了如何避免，之后同类问题再没出现过。
  </li>
  <li>
    <b>手柄支持</b>：后来才决定要同时支持手柄与 PC，导致部分操作没有及时适配，
    大部分测试也是在 PC 上做的，手柄成了次要考虑。
    最大的问题是某个小游戏在 PC 与主机上因为输入系统不同需要不同的实现方式，
    导致这个玩法在相当长一段时间里无法运行。
  </li>
  <li>
    <b>Unity 中途升级</b>：项目进行到一半时 Unity 爆出安全漏洞，全校被迫升级引擎版本。
    升级本身没有破坏任何东西，但部分在家工作的成员没有正确同步分支，造成了一些合并麻烦。
  </li>
  <li>
    <b>穿地抛竿（最常见的重复性 bug）</b>：玩家能隔着地面把鱼竿抛进水里。
    修复尝试了多次，消耗了大量时间。部分原因是<b>地图下方整片都是水</b>——
    海洋是一块巨大的平面，因此基础 raycast 永远会命中水面。
    最终通过更好的 raycast 与碰撞检测方式解决。
  </li>
</ul>
</section>

<section id="takeaways" title="总结" kicker="Takeaways">
<h3>做得好的（值得沿用到今后）</h3>
<ul>
  <li><b>Git Flow</b>：让我们始终拥有一个稳定的可玩版本。虽然合并有麻烦，但通过时间与培训可以缓解，整体是净收益。</li>
  <li><b>Scrum</b>：对项目规划帮助极大，让团队能掌握自己的进度，也让整个项目看起来没那么可怕。</li>
  <li><b>统一代码风格</b>：在项目开始就定下一致的代码风格，让阅读他人的代码简单很多——
    这也是行业里普遍做这件事的原因。</li>
</ul>

<h3>应该改进的</h3>
<ul>
  <li><b>Git 经验不足</b>：提交太少、只有一个人能合并与审查，根因都是缺少大规模项目的 Git 经验。</li>
  <li><b>资产管线（Asset Pipeline）</b>：美术资产耗时远超预期，原因是从建模软件到引擎的流转问题，以及优先级判断错误。
    一条可靠的资产管线能避免其中大部分问题。</li>
  <li><b>沟通</b>：很多开发中的问题来自简单的沟通不畅。在会议之外更好地交流，本可以加快开发、避免浪费时间修 bug。</li>
  <li><b>项目管理</b>：一开始选择了 Scrum 的自组织方式，这对大多数团队有效，但不是对所有人都有效。
    最后一刻提交 MR、功能没人主动认领，根源都是<b>不同的人需要不同的管理方式</b>。
    未来应该针对个人调整管理风格，而不是套用一种统一风格。</li>
</ul>

<h3>结论</h3>
<p>
  这个项目让所有成员获得了游戏设计行业的实际经验，也产出了一款可以放进作品集的完整作品。
  未来的项目里，<b>按工作板块（程序、美术等）而不是按人数来划分范围会更好</b>——
  我们在美术与内容量上过度扩张了，把范围对齐到每位成员的实际技能会得到更好的最终产品。
</p>
</section>
