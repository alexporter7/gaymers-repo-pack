# More Valuables Upgrade
[![GitHub](https://img.shields.io/badge/GitHub-MoreShopItems-brightgreen?style=for-the-badge&logo=GitHub)](https://github.com/InfusedGalaxy/MoreValuablesUpgrade)
[![Thunderstore Version](https://img.shields.io/thunderstore/v/GalaxyMods/MoreValuablesUpgrade?style=for-the-badge&logo=thunderstore&logoColor=white)](https://thunderstore.io/c/repo/p/GalaxyMods/MoreValuablesUpgrade)
[![Thunderstore Downloads](https://img.shields.io/thunderstore/dt/GalaxyMods/MoreValuablesUpgrade?style=for-the-badge&logo=thunderstore&logoColor=white)](https://thunderstore.io/c/repo/p/GalaxyMods/MoreValuablesUpgrade)

**Adds an upgrade that increases the valuable spawn count.**

## How It Works
**The loot spawns according to a positive animation curve (a graph in Unity that slopes upward), which means as the more stages you progress, the more loot naturally spawns. This mod takes those curves and multiplies each one by the increase factor. So, 1.1 is a 10% increase per upgrade acquired. 1.2 would be 20% increase per upgrade, and so on until 2, which is 100% increase in loot spawns per upgrade. I'd advise not setting it to anything above 1.3 since it scales quickly.

## Configuration
**This mod uses BULLETBOT's MoreUpgrades mod to store the config entries. Look under the MoreUpgrades config for this mods values.**

Below are the config values set up by MoreUpgrades
- Enabled: Whether the upgrade item can be spawned to the shop.
- Max Amount: The maximum number of times the upgrade item can appear in the truck.
- Max Amount In Shop: The maximum number of times the upgrade item can appear in the shop.
- Minimum Price: The minimum cost to purchase the upgrade item.
- Maximum Price: The maximum cost to purchase the upgrade item.
- Price Increase Scaling: The scale of the price increase based on the total number of upgrade item purchased.
- Max Purchase Amount: The maximum number of times the upgrade item can be purchased before it is no longer available in the shop.
- Allow Team Upgrades: Whether the upgrade item applies to the entire team instead of just one player.
- Starting Amount: The number of times the upgrade item is applied at the start of the game.
- Display Name: The display name of the upgrade item.

**More Valuables Upgrade dependent entry**
- Increase Factor: The amount of valuables to increase per upgrade bought.

**Note: This value is multiplicative and should NOT be set to numbers larger than 2.**

## Bug reports
https://github.com/InfusedGalaxy/MoreValuablesUpgrade/issues