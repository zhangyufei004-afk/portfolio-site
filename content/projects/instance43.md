---
slug: instance43
title: INSTANCE 43
subtitle: 把"针织"做成一套要管理空间位置的核心战斗循环
summary: 独立完成的 2D 俯视角动作 Demo。我主导角色战斗系统设计——攻击逻辑、技能槽位、成长天赋树，以及多套差异化敌人 AI 行为——并在 Unity 中用可运行原型验证每一个设计判断。核心机制是把一次攻击拆成"部署 + 回收"两个阶段，让玩家持续管理战场上的锚点位置。
year: "2026"
type: 2D 俯视角动作 · 战斗系统策划
role: 战斗系统设计 / 玩法原型 / 内容实现（独立完成）
team: 个人项目
duration: 2026（仓库提交记录 07-18 → 09-13）
engine: Unity 2D + C#
status: 可运行 Demo，已在 itch.io 发布可玩版本，代码开源
tags: ["Unity", "战斗系统", "系统策划", "敌人 AI", "成长树", "个人项目"]
cover: assets/img/instance43/cover.jpg
thumb: assets/img/instance43/cover.thumb.jpg
accent: "#6ee7a8"
order: 2
---

<section id="overview" title="项目概述" kicker="Overview">
<p>
  INSTANCE 43 是我独立完成的 2D 俯视角动作 Demo，覆盖从玩法原型到系统设计的完整流程。
  开发过程中我用 Codex 与 PixelLab 作为辅助工具，专注在<b>玩法原型构建、系统设计与内容实现</b>上。
</p>
<p>
  我最主要的自选命题是：<b>怎样让"角色差异"变成玩家每一局都要重新计算的空间决策</b>，
  而不是给他一套伤害更高或更快的技能。围绕着这个问题，我主导了角色战斗系统设计——
  攻击逻辑、技能槽位、成长天赋树——以及多套差异化的敌人 AI 行为逻辑。
</p>

<div class="links">
  <a class="btn btn--primary" href="https://yufei-zhang.itch.io/instance-43" target="_blank" rel="noopener noreferrer">
    下载试玩（itch.io） <span class="btn__hint">↗ 站外页面</span>
  </a>
  <a class="btn" href="https://github.com/zhangyufei004-afk/Instance-43" target="_blank" rel="noopener noreferrer">
    GitHub 仓库 <span class="btn__hint">↗ 站外页面</span>
  </a>
</div>

<h3>Demo 当前包含的可运行内容</h3>
<ul>
  <li>主菜单与场景入口</li>
  <li>实时战斗 HUD：生命、能量、技能槽位</li>
  <li>层间奖励选择与目标提示</li>
  <li>角色成长树与技能配置</li>
  <li>叙事对话与制作人员页面</li>
</ul>

<h3>项目的整体氛围设计</h3>
<p>
  主菜单用<b>高对比的绿色终端界面</b>叠加霓虹空间场景，先把项目的科幻氛围立起来，
  再把玩家导向开始游戏、机体成长和设置等入口。
</p>
<figure class="shot">
  <img src="assets/img/instance43/cover.jpg" alt="INSTANCE 43 主菜单：绿色终端界面叠加霓虹空间场景" loading="lazy" decoding="async">
  <figcaption>主菜单：终端式 UI 与霓虹场景的叠加，建立科幻基调</figcaption>
</figure>
</section>

<section id="combat-design" title="N-17 战斗系统策划案" kicker="Combat System Design">
<p>
  这份策划案要解决的问题是：<b>怎样让角色差异落实为可重复的空间决策</b>——
  部署、锚定、回收、爆发。
</p>

<h3>角色定位</h3>
<p>
  N-17 以可部署的<b>"针织"</b>为核心。攻击不是一次性投射，而是由
  <b>部署 → 固定 → 回收 → 织痕爆发</b>组成的循环。针织同时承担攻击、位移、护盾与战场锚点四种作用。
</p>

<div class="grid grid--2">
  <div class="pillar">
    <h3>四种战场价值</h3>
    <ul>
      <li><b>攻击</b>：沿路径造成伤害</li>
      <li><b>机动</b>：以针织为锚点位移</li>
      <li><b>防御</b>：消耗针织形成护盾</li>
      <li><b>爆发</b>：引爆敌人身上的织痕</li>
    </ul>
  </div>
  <div class="pillar">
    <h3>核心循环</h3>
    <p>
      战斗 → 攻击 / 移动 / 观察 → 击败敌人或生存 → 获得经验、货币和升级卡 →
      选择升级强化 → 进入下一场战斗。
    </p>
  </div>
</div>

<figure class="shot">
  <img src="assets/img/instance43/combat-loop-graph.jpg" alt="核心循环流程图" loading="lazy" decoding="async">
  <figcaption>核心循环流程图：从战斗到成长再回到战斗的闭环</figcaption>
</figure>

<figure class="shot">
  <img src="assets/img/instance43/enemies.jpg" alt="敌人设计板：多个敌人变体与其攻击表现" loading="lazy" decoding="async">
  <figcaption>敌人设计板：同一套行为框架下的多个变体与攻击表现</figcaption>
</figure>
</section>

<section id="attack" title="普通攻击：部署与回收的双阶段输入" kicker="Core Mechanic">
<p>
  这是整个设计里我最想讲清楚的一处判断：<b>把一次攻击拆成两个阶段</b>，
  目的不是让操作变复杂，而是让玩家必须持续管理战场上针织的位置。
</p>

<h3>单点模式</h3>
<p>
  每次点击只推进一枚针织；下一次输入<b>同时触发回收与下一枚发射</b>。
</p>
<div class="callout">
  <span class="callout__label">输入链路</span>
  <p>左键单击 → 发射 1 枚针织 → 固定于落点 → 再次点击并回收 → 沿原轨迹返回 / 路径伤害</p>
</div>

<h3>长按模式</h3>
<p>
  持续按住左键时连续部署；全部针织完成落点后，系统统一进入回收阶段。
</p>
<div class="callout">
  <span class="callout__label">输入链路</span>
  <p>左键长按 → 连续部署针织 → 全部完成部署 → 自动进入回收 → 沿轨迹返回 / 集中攻击</p>
</div>

<h3>设计意图</h3>
<blockquote>
  <p>
    回收不是攻击动画的尾段，而是 N-17 进行<b>空间管理、路径规划和时机判断</b>的核心操作。
  </p>
</blockquote>
<p>
  这条设计意图决定了后面所有数值和机制的走向：如果回收只是"收招动画"，
  那这两种输入模式就只是手感差异；只有当回收本身携带伤害、位移和护盾价值时，
  玩家才会真的去思考"我该把针织放在哪、什么时候收"。
</p>
</section>

<section id="ui" title="战斗 UI 与信息层级" kicker="Combat UI">
<figure class="shot">
  <img src="assets/img/instance43/hud-combat.jpg" alt="实时战斗 HUD：生命值、能量储备、四个技能槽位与目标指示" loading="lazy" decoding="async">
  <figcaption>实时战斗画面：生命值、能量储备、四个技能槽位与目标指示</figcaption>
</figure>

<p>
  画面同时展现玩家角色、敌方单位、目标指示、生命值显示、能量储备、四个技能槽位以及当前成长进度。
  我对布局的处理是把各项信息<b>推到屏幕边缘与战斗区域外围</b>，
  尽可能降低对主要战斗空间的视觉干扰。
</p>

<div class="callout">
  <span class="callout__label">我的设计决策</span>
  <p>
    当玩家需要同时理解"我还能承受多少伤害""技能是否可用""当前目标是谁"时，
    HUD 的设计应该<b>优先服务于决策制定，而不是单纯展示状态信息</b>。
  </p>
</div>

<p>基于这条原则，我把可见反馈收敛成四类：</p>
<ul>
  <li>生命值</li>
  <li>技能能量</li>
  <li>技能槽位</li>
  <li>目标提示</li>
</ul>

<figure class="shot">
  <img src="assets/img/instance43/combat-ui.jpg" alt="战斗中的另一处 UI 状态" loading="lazy" decoding="async">
  <figcaption>战斗中的另一处 HUD 状态：信息被放在战斗区域外围</figcaption>
</figure>
</section>

<section id="meta" title="成长树与路线选择" kicker="Meta Systems">
<h3>角色成长与技能配置</h3>
<p>
  技能页面将<b>攻击技能与战术技能划分为两个独立的配置槽位</b>，
  使玩家能够在进入高塔行动前预先规划并确定本局的能力组合。
</p>
<figure class="shot">
  <img src="assets/img/instance43/skill-config.jpg" alt="技能配置界面：攻击技能与战术技能两个独立槽位" loading="lazy" decoding="async">
  <figcaption>技能配置：攻击技能与战术技能分成两个独立槽位</figcaption>
</figure>

<p>
  成长页把<b>四条分支由中心节点延伸</b>，构成一条可视化的长期发展路径。
  我这样做的目的是让"选择什么"与"下一步如何成长"之间形成连贯的衔接关系——
  玩家在配置界面做决定时，能看见这个决定会把成长树推向哪里。
</p>
<figure class="shot">
  <img src="assets/img/instance43/growth-tree.jpg" alt="角色成长树：四条分支由中心节点延伸" loading="lazy" decoding="async">
  <figcaption>成长树：四条分支由中心节点延伸，形成可视化的长期路径</figcaption>
</figure>

<h3>楼层路线图与叙事节奏</h3>
<p>
  我把一局行动拆成<b>战斗、选择、推进和叙事停顿</b>四种节拍。玩家通关当前关卡后获得选择权，
  自主决定下一关要应对的战斗挑战；对话框则在战斗结束后穿插剧情内容，
  为故事的逐步展开营造氛围，同时激励玩家继续探索。
</p>
<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/instance43/route-choice.jpg" alt="楼层路线选择界面" loading="lazy" decoding="async">
    <figcaption>路线选择：通关后由玩家决定下一个战斗挑战</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/instance43/dialogue.jpg" alt="战斗间的叙事对话框" loading="lazy" decoding="async">
    <figcaption>叙事停顿：战斗之间穿插的对话与剧情推进</figcaption>
  </figure>
</div>
</section>

<section id="takeaways" title="反思" kicker="Takeaways">
<h3>先找到"这个角色独有的决策"，再设计技能</h3>
<p>
  N-17 的四种战场价值（攻击 / 机动 / 防御 / 爆发）全部挂在同一个载体——针织——上。
  这样玩家的每一次操作都在<b>同一个资源上做取舍</b>：把它用来打伤害，就没法同时用来位移或做护盾。
  这比给角色四个互不相关的技能更容易形成"这个角色该怎么打"的整体认知。
</p>

<h3>用可运行原型验证设计，而不是用文档说服自己</h3>
<p>
  这套双阶段输入如果只写在策划案里，看起来就是"两种操作模式"。
  真正把它做进 Unity 之后才发现：回收阶段的时长和路径判定，直接决定了玩家是"有意识地管理锚点"
  还是"在两个按钮之间乱按"。这类判断只能靠能跑的原型来回答。
</p>

<h3>HUD 是决策界面，不是状态显示屏</h3>
<p>
  把生命、能量、技能槽位和目标提示压到屏幕外围之后，玩家的视线才能真正留在战斗区域中央。
  这条经验后来在我做射击游戏的受击反馈与弹药 UI 时同样适用。
</p>

<h3>独立完成整条链路的价值</h3>
<p>
  从玩法原型、系统设计到内容实现都由我一个人走完，最大的收获是
  <b>能在设计阶段就判断"这个方案做起来要多久"</b>。
  比如针织的部署 / 回收两阶段，如果回收需要额外的轨迹物理模拟，
  成本会明显高于"沿原轨迹返回"——这种判断在只写文档时是得不出来的。
</p>
</section>
