# ScaleInCart
- Scales anything or valuables in the cart. 
- All players need to have the same config!
- Supports [REPOLib](https://thunderstore.io/c/repo/p/Zehs/REPOLib).
## Configuration
- **General**:
    - **Use Mass Scaling**: If enabled, valuables will scale based on their mass. If disabled, valuables will scale based on their valuable scale setting.
    - **Revert Back To Original Scale**: If enabled, valuables will revert to their original scale when not in the cart. If disabled, valuables will remain at their modified scale.
    - **Scale Everything**: If enabled, every grabbable object will be scaled. If disabled, only valuables will be scaled.
    - **Scale Speed**: The speed at which valuables scale down/up per update. Higher values make valuables shrink/expand faster.
    - **Scale Delay**: The initial delay in seconds before valuables begin scaling.
- **Mass Scaling**:
    - **Default Scale**: Default scale factor if no mass threshold is exceeded.
    - **Scale Factors**: Scaling factors for mass >= values. Format: `mass=scale`, separated by commas.
- **Modded Valuable Scaling**: Same as ***Valuable Scaling*** but for [REPOLib](https://thunderstore.io/c/repo/p/Zehs/REPOLib) valuables.
- **Valuable Scaling**: Controls the scaling factor for each valuable based on its scale.
    - **Use Valuable Scale**: If enabled, this will force the valuable scale to be used no matter what the "*Use Mass Scaling*" value would be.
    - **Valuable Scale**: Determines the scale factor for each valuable.