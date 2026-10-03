# INSTANCE 43 · 第一次 Build 的 Playtest 与迭代记录

**性质**：一**轮** playtest，**两位测试者**（同一版本、不同视角）
**验证方式**：改动均已通过阅读当前代码确认（仓库 `zhangyufei004-afk/Instance-43`）
**局限**：改动后**未再组织第二轮正式 playtest**（测试成本）

---

## 一、为什么这一轮测试特别有价值

两位测试者的关注点几乎不重叠，形成**互补的两个视角**：

| | 测试者 A | 测试者 B |
| --- | --- | --- |
| **关注层** | 体验层 —— 玩家怎么学会玩 | 机制层 —— 系统哪里坏了 |
| **反馈主题** | 新手引导、术语、信息传达 | 数值曲线、系统设计、技术缺陷 |
| **形式** | 成段论述（含因果分析） | 逐条清单（10 条） |

**一轮测试拿到两个互补视角**，且两人独立命中 4 组问题 —— 排除了"个别玩家口味"的可能。

---

## 二、两人独立命中的 4 组问题

### 问题 1 · 升级节奏与曲线失衡

| 测试者 | 原话 |
| --- | --- |
| **A** | "it felt like **I was spending most of my time selecting upgrades with only a few seconds of actual combat between them**" |
| **B** | "The upgrade cards at the start **didn't have too much effect** and at the end **just demolished everything**... it was a **jump in power**" |

**我的判断**：A 说的是**频率**（太密），B 说的是**幅度**（断层）。两个症状同一个根因 —— 升级投放没有和战斗节奏解耦，玩家在最需要连续操作的时候被打断。

**改动**：把升级从"战斗中强制弹出"改为**玩家主动开启**（见问题 3）。这一条同时改善了节奏与曲线感 —— 玩家可以打完一波再决定何时选升级，升级之间的战斗时间由玩家自己控制。

---

### 问题 2 · 玩家看不到进度信息

| 测试者 | 原话 |
| --- | --- |
| **A** | "I often **didn't know** how much of the current floor was left, **when I was going to receive another upgrade**" |
| **B** | "Pop up with level information is **too fast to go out the screen**, the first 15 minutes I ended up **going blindly**" |

**我的判断**：B 说的是**展示时长**，A 说的是**信息缺失**。合起来说明关卡进度的信息通道是断的 —— 不是"看不清"，是**缺少持续可见的进度锚点**。

**改动**：新增**升级可用提示面板**（常驻，直到玩家处理），替代原来一闪而过的弹窗。

---

### 问题 3 · 同一物理点击被拆成两个动作 ★ 根因修复

| 测试者 | 原话 |
| --- | --- |
| **A** | "an upgrade screen appeared while I was actively fighting. I pressed a number key intending to activate one of my abilities, but **that input immediately selected an upgrade instead**" |
| **B** | "Whenever I clicked with the mouse **it would make 2 clicks**, skipping dialogues and **instantaneously retracting the needles**" |

**我的判断**：两处症状同一个根因 —— **点击既是 UI 操作、又是战斗操作，两个系统都在监听同一次输入**。

具体链路：

```
玩家点击 → 推进对话框（UI 层响应）
         → 同一次点击被战斗层读作"开火"（GameInput.FireHeld）
         → 松开鼠标 → 触发回收
```

**后果比"手感差"严重得多**：针本该由玩家**主动决定何时回收**，被自动回收等于**核心机制的决策权被拿走了**。

**改动（三层防护）**：

**① 对话期间锁定战斗输入**

`PlayerShooting.Update` 在非 Gameplay 状态直接返回：

```csharp
if (GameManager.Instance != null
    && GameManager.Instance.CurrentState != GameManager.GameState.Gameplay) return;
```

对话开始时 `EndlessTowerTutorial` 把状态切到 `Transition`，战斗层随之停机，并同步复位动画与物理速度。

**② 修复"按键残留"边界情况 ← 这条是真正的难点**

即使锁了输入，还有一个隐蔽问题：**玩家点击时可能还按着鼠标**，关闭对话后战斗恢复，这个"按住"会被读成持续开火。

代码里有明确的处理（注释直接说明了这个场景）：

```csharp
// A mouse click can open/advance a modal presentation. Do not
// let the corresponding release be interpreted as an attack
// release when gameplay resumes on the reused player object.
suppressFireUntilRelease = true;
```

**③ 把"回收"改成完全独立的输入，并注释了设计意图**

```csharp
/// Explicit N-17 recall input. The primary attack is intentionally kept
/// independent from recall so releasing LMB never consumes the player's
/// planted Needle field.
public static bool RecallPressed => ...
    (Mouse.current.rightButton.wasPressedThisFrame) ...
```

```csharp
// Recall is deliberately a separate, explicit input. Releasing the
// primary attack never recalls the deployed anchors, which lets the
// player build a field and choose the exact payoff moment.
if (GameInput.RecallPressed) RecallAllNeedles(...);
```

**这一条最关键**：不是让自动回收更慢，而是**从输入映射层取消了它的可能** —— 松开左键在物理上不再能触发回收。

---

### 问题 4 · 术语与系统缺乏解释

| 测试者 | 原话 |
| --- | --- |
| **A** | "many important terms and mechanics are introduced **without explanation**, such as **Integrity, Natites, Anchors**" |

**我的判断**：A 描述的是一个**恶性循环** —— 术语没解释 → 看不懂升级 → 只能瞎选 → 无法建立 build 预期 → 更加看不懂。**术语不是文案问题，是玩法理解的入口。**

**改动**：新增**资料库（Database）系统** —— 可检索的系统说明与档案，玩家可以随时查阅术语、机体与机制。同时升级面板改为主动开启，玩家可以看明白再选。

---

## 三、B 单独提出的机制层问题

### B3 · 高塔路线选择没有意义 ⚠️

> "I would go for the **'risky route' every time and hardly ever anything happened**, be it good or bad. **The only exception was the route that helped focus the upgrades more for the build**, as it felt a little more impactful."

**归类**：风险回报设计

**我的判断**：**"高风险路线没有实际风险"意味着选择消失** —— 如果每次都该选它，它就不再是一个选择。

**而 B 补的这句话本身就是设计答案**：

> 玩家能感知到的差异是 **"对 build 的聚焦程度"**，而不是"风险量级"。

也就是说：**路线差异在「内容类型」维度上是有效的，在「风险大小」维度上是失效的。**

> 待补：这条的具体改动方式

### 其余单条反馈

| # | 问题 | 归类 | 状态 |
| --- | --- | --- | --- |
| B1 | 音乐音量过大（耳机 4% 仍需调低） | 音频混音 | 已处理 |
| B2 | 关卡结束后敌方子弹残留，关掉界面就被打 | 状态清理 | 已处理 |
| B4 | 精英怪只是换色，不足以成为关卡焦点 | 敌人设计 | 已处理 |
| B5 | 技能键位 1/2/3/4 不可改 | 输入可访问性 | 已处理（`SetAbilityKey` + `PlayerPrefs` 持久化） |
| B6 | 攻击技能冲击感弱 / 防御屏障可穿过 | 手感 + 碰撞一致性 | 已处理 |

---

## 四、两位测试者都肯定了同一件事

| 测试者 | 原话 |
| --- | --- |
| **A** | "Once I started understanding the systems, **the core combat concept worked well and was fun to use**. Firing the needles, positioning them, and recalling them through enemies gives the character **a more interesting combat loop than simply shooting continuously**." |
| **B** | "I know I just listed a lot of negative things, but honestly **the game was still really fun and enjoyable**... I would really like to see the end product." |

**两人在列完问题后都主动肯定了核心玩法。** A 的描述尤其重要 —— 他说"部署针 → 定位 → 穿过敌人回收"**比持续射击更有意思**，这正好是设计意图要达成的效果。

---

## 五、我提炼出的可迁移判断

### 1. 反馈要按"层"分类，而不是按"条"处理

10 条反馈混在一起，人只会想去修最吵的那条。按层归类后：

| 层 | 问题 | 影响 |
| --- | --- | --- |
| **技术层** | 点击被拆成两个动作 | 核心机制失效 |
| **机制层** | 路线无风险、精英怪定位失败 | 设计目标未达成 |
| **体验层** | 术语未解释、进度不可见 | 新玩家留存 |

**技术层最优先** —— 因为它让核心机制失效，其他优化都建立在"机制正常运行"之上。

### 2. "两人独立命中"是最高优先级的信号

| 优先级 | 判定依据 |
| --- | --- |
| **最高** | 两人独立命中（4 组） |
| 高 | 单人命中但属于**机制失效**（路线、残留弹幕） |
| 中 | 单人命中，**体验调优**（音量、键位） |
| 中 | 单人命中，**表现力不足**（精英怪、攻击手感） |

### 3. 根因比症状值钱

两份反馈里的"点击问题"看起来是两件事（一个说误选升级、一个说双击），实际上是**同一个根因**：UI 层与战斗层都在监听同一次输入。

**修根因只需一次改动就解决两个玩家的问题**，而分别去修症状会留下第三种触发方式。

### 4. 玩家给的不只是问题，还有答案

B 指出的"唯一有效的路线是聚焦 build 的那条"、A 指出的"这个战斗循环比持续射击有意思" —— **玩家自己指出了什么有效**。修改方向应该从"什么有效"往外推，而不是从"什么被骂"往里改。

---

## 六、这一轮的局限（如实记录）

- **改动后未再组织第二轮正式 playtest** —— 受测试成本限制
- 因此当前版本的问题是"**已按反馈修复，但未经独立验证**"
- 下一步应做的是**回归测试**：确认修复没有引入新问题，并验证路线风险与升级曲线是否真的改善了

> **这个局限本身就是设计判断的一部分** —— 知道自己"还没验证什么"，比声称"已经完美解决"更专业。
