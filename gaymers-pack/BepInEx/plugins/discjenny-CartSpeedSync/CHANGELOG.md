# Changelog

All notable changes to CartSpeedSync will be documented in this file.

## [2.0.0] - 2025-04-02

### Changed
- Refactored core logic to more closely replicate base game cart steering mechanics while sprinting.
- Ensured cart speed matches player speed during sprints to prevent bumping, integrating with base game logic.
- Increased responsiveness during sprint turns by adjusting base game velocity/rotation limits.
- Minimized physics glitches by moving away from direct force application and using base game's velocity manipulation.

## [1.1.0] - 2025-04-01

### Changed
- Adjusted cart follow distance when sprinting to better match base game behaviour.
- Tuned physics (force, rotation) specifically for small carts to improve handling during sprinting turns.

## [1.0.0] - 2025-03-31

### Added
- Initial release
- Cart speed matching when sprinting in strong push mode
- Improved cart positioning and turning behavior
- Smooth cart rotation during direction changes
- Automatic velocity clamping to prevent physics issues
- Support for both single player and multiplayer 