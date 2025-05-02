# Louder Hunter Footsteps for R.E.P.O.

**Version:** 1.0.0

Makes the Hunter enemy's footstep sounds configurable, allowing you to adjust their volume, audible range (falloff), and add an optional echo effect.

---

## Features

*   **Configurable Volume:** Make footsteps quieter or much louder (0.1x to 3.0x multiplier).
*   **Configurable Falloff:** Adjust how far the sound travels before fading out (0.2x to 5.0x multiplier).
*   **Optional Echo:** Add reverb to footsteps (if the level has reverb zones). Configurable mix amount.
*   All settings adjustable via the BepInEx config file.

---

## Installation

1.  Install BepInEx for R.E.P.O.
2.  Install this mod using r2modman or Thunderstore Mod Manager.
3.  Run the game once to generate the config file.

---

## Configuration

Edit the file `BepInEx/config/com.plusblankplus.louderhunterfootsteps.cfg` after running the game once.

*   `FootstepVolumeMultiplier`: Adjusts base volume (Default: 1.0).
*   `FootstepFalloffMultiplier`: Adjusts audible range (Default: 1.0).
*   `EnableFootstepEcho`: Set to `true` to enable echo (Default: false).
*   `FootstepEchoMix`: How much echo to apply (0.0 to 1.0, Default: 0.5). Requires `EnableFootstepEcho = true`.

---

## Source Code & License

Licensed under the **MIT License**.

---