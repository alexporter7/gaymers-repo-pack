---

## ⚠️ IMPORTANT NOTICE: CLIENT-SIDE MOD ⚠️  
**This mod is entirely client-side and does not affect gameplay or networking.**  
Other players do **not** need to install it for it to work properly in multiplayer.

---

[![Thunderstore Profile](https://img.shields.io/badge/Thunderstore-Profile-4065F2?style=for-the-badge&logo=thunderstore&logoColor=white)](https://thunderstore.io/c/repo/p/PxntxrezStudio/)
[![Thunderstore Version](https://img.shields.io/thunderstore/v/PxntxrezStudio/ValuableInspector?style=for-the-badge&logo=thunderstore&logoColor=white&color=40c4ff)](https://thunderstore.io/c/repo/p/PxntxrezStudio/ValuableInspector/)
[![Thunderstore Downloads](https://img.shields.io/thunderstore/dt/PxntxrezStudio/ValuableInspector?style=for-the-badge&logo=thunderstore&logoColor=white&color=00e111)](https://thunderstore.io/c/repo/p/PxntxrezStudio/ValuableInspector/)

---

> **If you like my work, you can:** [![DonationAlerts](https://i.imgur.com/OMyWf9T.png)](https://www.donationalerts.com/r/pxntxrez)

# Valuable Inspector

A HUD overlay mod for R.E.P.O. that displays live information about the **valuable object you're currently holding**.

## Features

-  Displays **Name**, **Value Range**, **Weight**, and **Stuns On Hit**
- Fully customizable UI:
  - Size, position, font, shadow
  - Colors via RGB sliders
  - Optional auto-resizing
  - Configurable via BepInEx config or in-game with [**REPOConfig**](https://thunderstore.io/c/repo/p/nickklmao/REPOConfig/)

## Compatibility

- Supports valuables from **Other Mods**

## Installation

1. Install [BepInEx](https://thunderstore.io/c/repo/p/BepInEx/BepInExPack/) For R.E.P.O.
2. Place the `ValuableInspector.dll` in your `BepInEx/plugins` folder
3. Launch the game

## Configuration Options
 💡 **Recommended:** Install the [**REPOConfig**](https://thunderstore.io/c/repo/p/nickklmao/REPOConfig/) mod to change these settings directly in-game via a GUI.

**Located in:**  
`BepInEx/config/Pxntxrez.ValuableInspector.cfg`

Below are all available configuration options.

---

### 🔹 Debug Options

| Setting | Description | Default |
|--------|-------------|---------|
| `RemoveCloneSuffix` | Remove `(Clone)` from valuable names. | `true` |
| `RemoveValuablePrefix` | Remove `"Valuable "` prefix from names. | `true` |
| `CapitalizeNameWords` | Capitalize each word in the item name (e.g., `golden apple` → `Golden Apple`) | `false` |

---

### 🔹 Display Options

| Setting | Description | Default |
|--------|-------------|---------|
| `ShowName` | Show the name of the valuable. | `true` |
| `ShowValue` | Show the value range (min–max). | `true` |
| `ShowWeight` | Show the weight. | `true` |
| `ShowStunInfo` | Show which enemies the item can stun based on weight. | `false` |

---

### 🔹 UI Position Settings

| Setting | Description | Default |
|--------|-------------|---------|
| `UIPreset` | UI anchor preset: `BottomRight`, `BottomLeft`, `TopLeft`, `TopRight`, `TopCenter` | `TopCenter` |
| `OffsetX` | Horizontal position offset. | `1` |
| `OffsetY` | Vertical position offset. | `66` |

💡 By default, the UI appears at the **top-center of the screen**.
You can reposition it using `UIPreset`, `OffsetX`, and `OffsetY`.

---

### 🔹 UI Settings

| Setting | Description | Default |
|--------|-------------|---------|
| `BoxWidth` | Width of the info box. *(Ignored when `AutoResize` is enabled)* | `500` |
| `BoxHeight` | Height of the info box. *(Ignored when `AutoResize` is enabled)* | `225` |
| `FontSize` | Font size of the info text. *(1–60)* | `28` |
| `FontStyle` | Font style (Normal, Bold, Italic, BoldAndItalic). | `Bold` |
| `AutoResize` | Automatically resize the box to fit text content. **Disables BoxWidth and BoxHeight.** | `true` |
| `ShadowOffset` | Offset of the text shadow. *(Vector2)* | `2,2` |

💡 **Note:** When `AutoResize` is enabled, `BoxWidth` and `BoxHeight` are ignored and the box resizes automatically to fit the text.

---

### 🔹 Color Settings (RGB 0–255)

| Setting | Description | Default |
|--------|-------------|---------|
| `TextColorR` | Red component of text color. | `255` |
| `TextColorG` | Green component of text color. | `255` |
| `TextColorB` | Blue component of text color. | `255` |
| `BackgroundColorR` | Red component of background color. | `0` |
| `BackgroundColorG` | Green component of background color. | `0` |
| `BackgroundColorB` | Blue component of background color. | `0` |
| `ShadowColorR` | Red component of shadow color. | `0` |
| `ShadowColorG` | Green component of shadow color. | `0` |
| `ShadowColorB` | Blue component of shadow color. | `0` |

---

## Stun Mechanics (Based on Weight)

This is how the mod determines which enemies get stunned when hit with a valuable:

| Weight Range | Can Stun |
|--------------|----------|
| `0.5 – 1.9`  | ✅ SHADOW CHILD, SPEWER, RUGRAT, ANIMAL, UPSCREAM, CHEF, HIDDEN |
| `2.0+`       | ✅ BOWTIE, MENTALIST, HEADMAN, ROBE, HUNTSMAN, REAPER, CLOWN, TRUDGE |

> ⚠️ **Exception:**  
> `DUCK` and `PEAPER` **cannot be stunned** by any valuable, regardless of weight (even 8.0+).

## Developer Contact
**Report bugs, suggest features, or provide feedback:**

| **Discord Server** | **Channel** | **Post** |  
|--------------------|-----------|----------|  
| [R.E.P.O. Modding Server](https://discord.com/invite/vPJtKhYAFe) | `#released-mods` | [Valuable Inspector](https://discord.com/channels/1344557689979670578/1366740609376976918) |