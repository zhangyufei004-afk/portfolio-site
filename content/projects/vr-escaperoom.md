---
slug: vr-escaperoom
title: VR Escape Room
subtitle: 在 VR 里做谜题、交互与流程状态机
summary: Unity / VR 密室逃脱项目。我负责 VR 交互设计、关卡谜题逻辑、用户体验优化与游戏主流程的状态机控制，并参与 3D 资产制作与团队交付。玩家被锁在一间神秘的房间里，唯一的出路是解开隐藏在房间中的谜题。
year: "2025"
type: VR 交互与谜题设计
role: VR 游戏设计师兼核心开发者
team: 团队项目
duration: 2025.02 – 2025.06
engine: Unity + C# / Blender / Autodesk Fusion
status: 已完成课程项目
tags: ["Unity", "VR", "交互设计", "谜题设计", "状态机"]
cover: assets/img/vr-escaperoom/cover.jpg
thumb: assets/img/vr-escaperoom/cover.thumb.jpg
accent: "#8fb8f0"
order: 8
---

<section id="overview" title="项目概述" kicker="Overview">
<p>
  VR Escape Room 是一个 Unity + VR 的密室逃脱项目。开场叙事把目标交代得很直接：
</p>
<blockquote>
  <p>
    You find yourself locked inside a mysterious room.<br>
    The only way out is to solve the puzzles hidden within.<br>
    Look closely, think carefully, and pay attention to every detail —<br>
    only the cleverest will find the way to escape.<br>
    <b>Good luck!</b>
  </p>
</blockquote>
<p>
  我在团队中担任 <b>VR 游戏设计师兼核心开发者</b>，负责的范围覆盖交互、谜题、体验和流程四个层面。
</p>

<div class="links">
  <a class="btn" href="https://eng-git.canterbury.ac.nz/yzh440/prod223-25s1-escaperoom" target="_blank" rel="noopener noreferrer">
    项目仓库（校内 EngGit） <span class="btn__hint">↗ 需要校内账号</span>
  </a>
</div>

<figure class="shot">
  <img src="assets/img/vr-escaperoom/briefing.jpg" alt="开场叙事文字：玩家被锁在神秘房间里" loading="lazy" decoding="async">
  <figcaption>开场叙事：用一段文字交代目标与基调，再交还控制权</figcaption>
</figure>
</section>

<section id="role" title="我的职责" kicker="Role">
<div class="table-scroll">
<table>
  <thead><tr><th>方向</th><th>具体工作</th></tr></thead>
  <tbody>
    <tr>
      <td><b>VR 交互</b></td>
      <td>用 Unity 与 C# 开发互动式 VR 游戏，构建高沉浸感的虚拟环境与<b>符合直觉的 VR 手势交互</b>。</td>
    </tr>
    <tr>
      <td><b>谜题与流程</b></td>
      <td>全权负责关卡解谜逻辑、用户体验（UX）优化，以及游戏主流程的<b>状态机控制</b>。</td>
    </tr>
    <tr>
      <td><b>3D 资产</b></td>
      <td>用 Blender 与 Autodesk Fusion 完成 3D 资产的建模、材质处理与动画制作，并无缝导入引擎。</td>
    </tr>
    <tr>
      <td><b>团队交付</b></td>
      <td>在团队开发环境中紧密协作，推进项目进度，保证所有里程碑节点的高质量交付。</td>
    </tr>
  </tbody>
</table>
</div>

<h3>为什么用状态机管理流程</h3>
<p>
  VR 密室逃脱的流程比普通关卡更容易失控：玩家可能同时触发多个交互、中途摘下头显、
  或者在谜题未完成时移动到下一个区域。把主流程收敛成显式状态机，是为了让
  "当前处于哪个阶段、哪些交互应该可用"永远有唯一答案，
  而不是散落在各个物件的 <code>Update()</code> 里互相打架。
</p>
</section>

<section id="spaces" title="房间与交互" kicker="Rooms &amp; Interaction">
<p>
  关卡由多个<b>用颜色做了强区分</b>的房间构成。这种做法在 VR 里尤其有效：
  玩家没有小地图可看，颜色是他建立空间记忆最直接的抓手——
  回头找路时，他记住的是"那面红墙的房间"，而不是抽象的方向。
</p>

<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/vr-escaperoom/room-red.jpg" alt="红色房间的俯视视角" loading="lazy" decoding="async">
    <figcaption><b>红色房间</b>：进入后的第一个空间，地面与墙面用强色块区分</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/vr-escaperoom/room-red-close.jpg" alt="白色拉杆与齿轮机关" loading="lazy" decoding="async">
    <figcaption><b>可交互机关</b>：白色拉杆与齿轮，配合红色激光指示</figcaption>
  </figure>
</div>

<figure class="shot">
  <img src="assets/img/vr-escaperoom/cover.jpg" alt="白色书架谜题与玩家的 VR 双手" loading="lazy" decoding="async">
  <figcaption>
    <b>书架谜题</b>：白色书架上有若干可交互物件，画面右下角是玩家的 VR 双手与激光指针——
    这是我负责的"交互可读性"部分：玩家必须一眼看出哪些东西能拿、能推。
  </figcaption>
</figure>

<h3>交互设计的核心问题</h3>
<p>
  VR 里没有鼠标指针。玩家判断一个物件能不能交互，完全依赖它的造型、位置和现有反馈。
  所以"可交互性"必须在场景美术阶段就被设计进去，而不是等到交互逻辑写完再回头补——
  这也是我在这个项目里最花时间的一处权衡。
</p>
</section>

<section id="puzzles" title="谜题机制" kicker="Puzzle Mechanics">
<p>
  谜题按"观察 → 操作 → 反馈"三段来设计，且刻意控制了思考步数。
</p>

<div class="gallery gallery--2">
  <figure class="shot">
    <img src="assets/img/vr-escaperoom/puzzle-buttons.jpg" alt="彩色按钮与圆形转盘机关" loading="lazy" decoding="async">
    <figcaption><b>彩色按钮谜题</b>：四个彩色按钮与中央圆形机关，玩家需要在房间各处找到对应线索</figcaption>
  </figure>
  <figure class="shot">
    <img src="assets/img/vr-escaperoom/puzzle-dial.jpg" alt="转盘机关的俯视视角" loading="lazy" decoding="async">
    <figcaption><b>俯视视角</b>：转盘与按钮的相对位置关系是解谜的关键信息</figcaption>
  </figure>
</div>

<figure class="shot">
  <img src="assets/img/vr-escaperoom/room-laser.jpg" alt="贯穿房间的红色激光" loading="lazy" decoding="async">
  <figcaption><b>激光线索</b>：红色激光束跨越房间，同时承担"引导视线"和"叙事暗示"两个作用</figcaption>
</figure>

<h3>难度预算比平面游戏更低</h3>
<p>
  戴着头显做空间推理的认知负担明显高于平面游戏：玩家要同时处理真实身体的平衡、
  手柄的握持、以及虚拟空间里的方位。所以我把谜题的"思考步数"控制在比同等难度的
  2D 关卡更少的水平，把难度转移到<b>观察的细致程度</b>上——
  线索都看得见，但需要真的留意细节。这也正好呼应了开场那句
  "look closely, think carefully, and pay attention to every detail"。
</p>
</section>

<section id="takeaways" title="反思" kicker="Takeaways">
<h3>流程控制是 VR 项目里最容易被低估的工作</h3>
<p>
  在平面游戏里，一个"现在还不能用"的交互按钮，玩家按了没反应通常也能理解。
  但在 VR 里，玩家的手是真的伸过去了——没有反馈会被解读成"这游戏坏了"。
  把主流程写成显式状态机之后，我才能保证每个阶段的可交互物集合是确定的，
  并且能给"暂时不可用"提供明确反馈。
</p>

<h3>UX 优化的实际工作量往往超过谜题本身</h3>
<p>
  抓取手感、手腕角度、物件吸附范围这些细节，才是决定体验评价的部分。
  谜题逻辑一旦跑通就基本不再变动，但这些手感参数我一直在反复调。
</p>

<div class="callout">
  <span class="callout__label">素材说明</span>
  <p>
    页面里的截图来自当时的 Unity 编辑器录屏（原始画质 854×480）。
    它们记录了真实的交互与谜题状态，但分辨率不高——如果你之后找到更高清的录屏或头显内录，
    给我我替换掉。
  </p>
</div>
</section>
