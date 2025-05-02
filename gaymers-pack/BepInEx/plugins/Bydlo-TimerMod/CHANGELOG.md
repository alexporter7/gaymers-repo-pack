# v1.1.1
- Fixed wrong enemy timer display on client side.
  - Due to the fact that respawn times (as almost all enemy logic) is executing on host's side, there is no reasonable way to get this time from host, especially if host don't have Mod. So i ended up with this solution: if you are not a host, you will only see alive/dead status of an enemy. Respawn announcements working normally.

# v1.1.0
- Added configuration
- Added(fixed) message when enemy respawned (in bottom right)

# v1.0.0
- Initial release