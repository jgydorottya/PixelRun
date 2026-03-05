import os
import pygame
from src.sprites.ground import Ground
from src.sprites.obstacle import Obstacle
from src.sprites.reward import Reward
from src.components.portal import Portal

# assets directory
assets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')

ground_start = os.path.join(assets_dir, 'ground', 'ground_start.png')
ground_image = os.path.join(assets_dir, 'ground', 'ground.png')
ground_end = os.path.join(assets_dir, 'ground', 'ground_end.png')
ground_block = os.path.join(assets_dir, 'ground', 'ground_block.png')
spike = os.path.join(assets_dir, 'obstacle', 'spike.png')
wheel = os.path.join(assets_dir, 'obstacle', 'wheel.png')
cherry = os.path.join(assets_dir, 'reward', 'cherry.png')
grape2 = os.path.join(assets_dir, 'reward', 'grape2.png')
orange = os.path.join(assets_dir, 'reward', 'orange.png')
portal_entry = os.path.join(assets_dir, 'portal', 'portal_entry.png')
portal_exit = os.path.join(assets_dir, 'portal', 'portal_exit.png')

# Grounds
grounds = pygame.sprite.Group()
x = 0 
for i in range(0, 13):
    if(i == 0 or i == 6):
        ground = Ground(x, 780, 176, 176, ground_start)
    elif(i == 5 or i == 12):
        ground = Ground(x, 780, 176, 176, ground_end)
        x += 200
    else:
        ground = Ground(x, 780, 176, 176, ground_image)
    grounds.add(ground)
    x += 176

x -= 24
ground = Ground(x, 780, 176, 176, ground_block)
grounds.add(ground)
x_reward3 = x-100
x += 2*176
x_reward4 = x-100

for i in range(0, 10):
    if(i == 0):
        ground = Ground(x, 780, 176, 176, ground_start)
    elif(i == 9):
        ground = Ground(x, 780, 176, 176, ground_end)
    else:
        ground = Ground(x, 780, 176, 176, ground_image)
    grounds.add(ground)
    x += 176

# # Obstacles
obstacles = pygame.sprite.Group()
obstacle1 = Obstacle(620, 752, 64, 28, spike)
obstacle2 = Obstacle(684, 752, 64, 28, spike)
obstacle3 = Obstacle(1600, 752, 64, 28, spike)
obstacle4 = Obstacle(1830, 752, 64, 28, spike)
obstacle5 = Obstacle(2060, 752, 64, 28, spike)
obstacles.add([obstacle1, obstacle2, obstacle3, obstacle4, obstacle5])

obstacles_behind = pygame.sprite.Group()
obstacl1 = Obstacle(x_reward4+500, 770, 114, 111, wheel, rotating = True)
obstacl2 = Obstacle(x_reward4+1100, 770, 114, 111, wheel, rotating = True)
obstacles_behind.add([obstacl1, obstacl2])
obstacles_behind.add(obstacl2)

# # Rewards
reward1 = [650, 570, 52, 60, cherry]
reward2 = [1130, 570, 44, 52, grape2]
reward3 = [x_reward3, 570, 52, 60, cherry]
reward4 = [x_reward4, 570, 52, 60, cherry]
reward5 = [x_reward4+800, 700, 44, 52, grape2]
reward6 = [1620, 570, 36, 56, orange]
reward7 = [1850, 570, 36, 56, orange]
reward8 = [2080, 570, 36, 56, orange]
rewards = [reward1, reward2, reward3, reward4, reward5, reward6, reward7, reward8]

def get_rewards():
    reward = pygame.sprite.Group()
    for i in rewards:
        reward.add(Reward(i[0], i[1], i[2], i[3], i[4]))
    return reward

# Portals
portal_entry = Portal(128, 522, 252, 384, portal_entry)
portal_exit = Portal(x-350, 522, 252, 384, portal_exit)

cow_char = os.path.join(assets_dir, 'character', 'cow_char.png')
startgame_button = os.path.join(assets_dir, 'button', 'startgame_button.png')
quit_button = os.path.join(assets_dir, 'button', 'quit_button.png')
yes_button = os.path.join(assets_dir, 'button', 'yes_button.png')
no_button = os.path.join(assets_dir, 'button', 'no_button.png')
resume_button2 = os.path.join(assets_dir, 'button', 'resume_button2.png')
backtomenu_button2 = os.path.join(assets_dir, 'button', 'backtomenu_button2.png')
joystix_monospace = os.path.join(assets_dir, 'font', 'joystix-monospace.otf')
sinnesloschen_beam = os.path.join(assets_dir, 'music', 'sinnesloschen-beam.mp3')
start_bg = os.path.join(assets_dir, 'background', 'start_bg.png')
gameover_bg1 = os.path.join(assets_dir, 'background', 'gameover_bg1.png')
stop_bg = os.path.join(assets_dir, 'background', 'stop_bg.png')
game_bg = os.path.join(assets_dir, 'background', 'game_bg.png')
congrats_bg = os.path.join(assets_dir, 'background', 'congrats_bg.png')