# R.E.P.O 治疗无人机模组 / R.E.P.O Heal Drone Mod



## 模组简介 / Overview
基于游戏内无人机模型制作的治疗无人机模组，可自动跟随玩家并持续恢复生命值。  
**高度可定制化**的配置系统，满足不同玩家的需求！  
Heal Drone mod based on in-game drone model, automatically follows players and provides continuous health regeneration.  
**Fully customizable** configuration system for personalized gameplay!

---

## 🛠️ 安装方法 / Installation
1. 将以下文件放入 `BepInEx/plugins` 目录：  
   Place these files in `BepInEx/plugins`:
   - `REPO_HealDrone.dll`
   - `repo_healdrone` 文件夹  
   📌 确保两个文件在**同一目录**下  
   Ensure both files are in the ​**same directory**

---

## ⚙️ 配置文件 / Configuration
**路径 Path**: `BepInEx/config/com.Xiaohai.REPO.HealDrone.cfg`

| 配置项 (中文) | Configuration (English) | 类型 Type | 默认值 Default |
|--------------|--------------------------|-----------|---------------|
| UI显示物品名字<br>（多语言支持） | Display item names in UI<br>(Multilingual support) | String | `治疗无人机` |
| 治疗时间间隔<br>（单位：秒） | Treatment interval<br>(in seconds) | Int32 | `2` |
| 单次治疗量 | Heal amount per cycle | Int32 | `1` |
| 电池消耗率<br>（最大值100） | Battery drain rate<br>(Max 100) | Single | `0.5` |
| 治疗特效<br>（间隔≥5秒推荐） | Healing VFX<br>(Recommended when interval ≥5s) | Boolean | `false` |
| 首关默认生成 | Spawn in first level by default | Boolean | `true` |

---

## 🔧 配置示例 / Example Settings
```ini
# 沉浸式体验配置（适合高难度游戏）
HealEffect = true      # 启用华丽治疗特效
Treatment Interval = 5  # 每5秒治疗一次
healAmount = 3         # 每次恢复3点生命值
```

---
![游戏内实拍图](https://imgur.com/uimNGjd.png)
## 📜 开发者信息 / Developer Info
**作者 Author**: 小海 (XiaoHai)  
**Bilibili**: [点击访问主页](https://space.bilibili.com/2055787437)

**当前版本 Version**:  
- `V1.0.0` - 初始稳定版发布  
First stable release with core healing functionality
- `V1.0.2` - 修复了多人游戏中无法治疗他人
Fixed cant heal other player
---

💡 ​**提示 / Tip**: 修改配置后需**重启游戏**生效  
Requires ​**game restart** after config changes