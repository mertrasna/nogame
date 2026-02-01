# 🛠️ Nogame: Development Roadmap

This document outlines the features and polish remaining for the **Asinbase: Nogame** prototype.

## 🔴 High Priority: Combat Feel
- [ ] **Hit Flash Effect:** Implement a shader or white-surface tint when a player takes damage.
- [ ] **Knockback Physics:** Apply a small horizontal force (`dx`) to a player when they are hit to prevent "hugging."
- [ ] **Screen Shake:** Add a small camera jitter when a "heavy" attack connects.
- [ ] **Hurt Box Refinement:** Make the character's body hitbox (`rect`) smaller than the sprite art to allow for "near misses."

## 🟡 Medium Priority: Systems
- [ ] **Configuration File:** Move player stats (HP, Speed, Damage) to a `config.json` or `settings.py` dict.
- [ ] **Round System:** Add a "Best of 3" counter with icons under the health bars.
- [ ] **Character Select:** Create a simple menu state to choose between Arthur, Merlin, or future fighters.
- [ ] **Sound FX:** Integrate `pygame.mixer` for sword swings, hit impacts, and victory music.

## 🟢 Low Priority: Polish & Visuals
- [ ] **Parallax Background:** Split the background into layers that move at different speeds.
- [ ] **Particle Effects:** Add dust clouds when jumping and "sparks" when swords collide.
- [ ] **Dynamic Shadows:** Draw a simple oval shadow on the floor that stays at `FLOOR_Y`.
- [ ] **KO Slow Motion:** Briefly lower the FPS or use a timer to slow the game down during the final hit.

---
