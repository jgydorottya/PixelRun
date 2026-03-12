# PixelRun

PixelRun is a 2D pixel-art platformer built with Python and Pygame.

Jump over obstacles, collect rewards, and reach the exit portal to complete the level.

---

## Features
- Fullscreen 2D platformer gameplay
- Retro pixel-art style
- Collectible rewards that increase the final score
- Obstacles, gaps, rotating hazards, and portals
- Multiple game states: Start Menu, Gameplay, Pause, Game Over, and Congrats
- Keyboard controls for movement, jumping, pausing, and menu navigation

---

## Controls
- A - move left
- D - move right
- Space - jump
- Escape - pause the game
- Enter - return to main menu from final screen

---

## Project Structure

- `main.py` - initializes Pygame, loads assets, handles scenes, input, collisions, reward counting, and the main game loop
- `src/sprites/character.py` - player character logic and collision checks
- `src/sprites/ground.py` - ground/platform sprites
- `src/sprites/obstacle.py` - static, moving, and rotating obstacles
- `src/sprites/reward.py` - collectible reward items
- `src/components/button.py` - UI buttons
- `src/components/portal.py` - level start/end portals
- `src/levels/level_1.py` - level layout, assets, rewards, portals, and obstacle placement

---

## Gameplay
The player starts from the entry portal and must cross the level by avoiding obstacles and falling off the map. Rewards can be collected during jumps and movement, and the final reward count is shown after successfully finishing the level.

---

## Tech Stack
- Python
- Pygame
- Pixel-art assets for the game, created in Pixilart
- Structured with reusable sprite/component classes

---

## Notes
The current version focuses on a single playable level, but the codebase is already separated into level and component files, which makes future expansion easier.

---

## Possible Improvements
- Add more levels and increasing difficulty
- Add a 'How to play' screen in the menu
- Save and display high scores
- Add multiple unlockable characters
