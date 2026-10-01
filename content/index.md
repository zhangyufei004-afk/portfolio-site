---
hero_title: 游戏设计 / 关卡设计 / AI 系统
hero_sub: 我是张宇飞，坎特伯雷大学游戏设计专业学生。我习惯把"设计意图"拆成可验证的系统——AI 状态机、关卡节奏、玩家引导——然后用 playtest 数据一轮轮把它逼到能成立。
body_class: page-home
---

<section class="section section--plain">
  <p class="lede">
    这里收录了九个项目。有独立完成的动作 Demo（INSTANCE 43）与四个单人关卡设计项目：从 Unity 里的潜行恐怖 AI（ECHOES），
    到 Unreal 的潜入关卡、Portal 2 解谜测试室、以及塞尔达式 2D 地牢；
    也有三段六人团队协作经历（Bounty Hunter、Stormhaven、Cozy Fishing）与一个 VR 密室逃脱项目。
    每个页面都保留了每一轮 playtest 的反馈和对应的修改——因为那些修改才是真正的设计工作。
  </p>
  <div class="stats">
    <div class="stat"><span class="stat__num">9</span><span class="stat__label">个已归档项目</span></div>
    <div class="stat"><span class="stat__num">5</span><span class="stat__label">个独立完成的项目</span></div>
    <div class="stat"><span class="stat__num">4</span><span class="stat__label">个团队协作项目</span></div>
    <div class="stat"><span class="stat__num">6</span><span class="stat__label">个引擎 / 编辑器</span></div>
  </div>
</section>

<section class="section section--plain">
  <header class="section__head">
    <p class="section__kicker">精选</p>
    <h2 class="section__title">先看这三个</h2>
  </header>
  <div class="grid grid--cards grid--flush">

    <a class="card card--feature" href="projects/echos/">
      <div class="card__thumb">
        <img src="assets/img/echos/cover.thumb.jpg" alt="ECHOES 游戏画面" loading="lazy" decoding="async">
        <span class="card__badge">最新</span>
      </div>
      <div class="card__body">
        <p class="card__meta">2026 · 潜行恐怖 / AI</p>
        <h3 class="card__title">ECHOES</h3>
        <p class="card__summary">
          在漆黑迷宫里被一只对光和声音有反应的怪物追杀。核心是一套 Patrol / Suspicious / Chase / Attack 有限状态机，
          配合 NavMesh 寻路与躲藏机制。
        </p>
        <div class="card__tags">
          <span class="tag tag--sm">Unity</span>
          <span class="tag tag--sm">FSM</span>
          <span class="tag tag--sm">NavMesh</span>
          <span class="tag tag--sm">单人项目</span>
        </div>
      </div>
    </a>

    <a class="card card--feature" href="projects/als/">
      <div class="card__thumb">
        <img src="assets/img/als/cover.thumb.jpg" alt="Unreal ALS 潜入关卡画面" loading="lazy" decoding="async">
      </div>
      <div class="card__body">
        <p class="card__meta">2026 · 关卡设计 / 潜入</p>
        <h3 class="card__title">ALS 潜入关卡「Infiltration」</h3>
        <p class="card__summary">
          Unreal Engine 5 + ALS 运动系统。垂直攀爬潜入 → 服务器房潜行 → 触发警报后限时逃离，
          并用"能量弓按钮链"把机制做出新用法。
        </p>
        <div class="card__tags">
          <span class="tag tag--sm">Unreal Engine 5</span>
          <span class="tag tag--sm">潜行</span>
          <span class="tag tag--sm">叙事化引导</span>
        </div>
      </div>
    </a>

    <a class="card card--feature" href="projects/stormhaven/">
      <div class="card__thumb">
        <img src="assets/img/stormhaven/vista-spline.thumb.jpg" alt="Stormhaven 的 Vista Actor 与 spline 路径" loading="lazy" decoding="async">
      </div>
      <div class="card__body">
        <p class="card__meta">2025 · 团队项目 / Unreal</p>
        <h3 class="card__title">Stormhaven</h3>
        <p class="card__summary">
          六人团队、六周打磨期。为探索类原型补上 Vista 电影镜头与快速旅行网络，并扩展叙事。
          我负责 FPS 系统强化：HUD 重设计、血腥屏、武器动画与敌人 AI。
        </p>
        <div class="card__tags">
          <span class="tag tag--sm">Unreal Engine</span>
          <span class="tag tag--sm">蓝图</span>
          <span class="tag tag--sm">FPS 系统</span>
          <span class="tag tag--sm">敌人 AI</span>
        </div>
      </div>
    </a>

  </div>
  <p class="morelink"><a href="works.html">查看全部 9 个项目 →</a></p>
</section>

<section class="section section--plain">
  <header class="section__head">
    <p class="section__kicker">我关注什么</p>
    <h2 class="section__title">三条一直在重复的线索</h2>
  </header>
  <div class="grid grid--3">
    <div class="pillar">
      <h3>引导是设计责任，不是 UI 任务</h3>
      <p>
        2D 地牢的房间编号、Portal 2 的 antline、Unreal 关卡墙上的 AR 警示文字——
        同一个问题在不同尺度上反复出现：玩家看不见你的意图，再好的机制也不成立。
      </p>
    </div>
    <div class="pillar">
      <h3>对抗"人为难度"</h3>
      <p>
        敌人堆砌、过窄的限时、过大的伤害判定盒，本质都是"惩罚代替设计"。
        我的解法很一致：收紧约束、强化引导、重排节奏。
      </p>
    </div>
    <div class="pillar">
      <h3>系统的鲁棒性优先于复杂度</h3>
      <p>
        一次卡死足以毁掉整段体验，一次偷懒的合并请求足以拖垮整个流程。
        我习惯先把"安全网"做出来，再叠加创意。
      </p>
    </div>
  </div>
</section>
