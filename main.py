import os
import pygame
import sys
from src.sprites.character import Character
from src.components.button import Button
from src.levels.level_1 import grounds, obstacles, get_rewards, obstacles_behind, portal_entry, portal_exit, cow_char, startgame_button, quit_button, yes_button, no_button, resume_button2, backtomenu_button2, joystix_monospace, sinnesloschen_beam, start_bg, gameover_bg1, stop_bg, game_bg, congrats_bg

pygame.init()

# Set up display
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption('Pixel Run')

clock = pygame.time.Clock()

alpha = 255
direction_alpha = -5

# Character
character = Character(200, 685, 108, 100, cow_char)
character_is_jumping = False
character_jump_count = 0
character_direction = 1

# Buttons
button_start = Button(622, 505, 676, 112, startgame_button)
button_quit = Button(820, 685, 280, 112, quit_button)
button_yes = Button(650, 630, 212, 104, yes_button)
button_no = Button(1060, 630, 152, 104, no_button)
button_resume = Button(677, 285, 565, 130, resume_button2)
button_back = Button(561, 545, 798, 114, backtomenu_button2)

# scene 1 = start menu
# scene 2 = jatek
# scene 3 = pause menu
# scene 4 = game over
# scene 5 = congrats
scene = 1

def game_over():
    global scene
    scene = 4

offset_x = 0
offset_y = 0

# Jump settings
jump_frames = 18
jump_height = 18
fall_height = 13

# Fonts
reward_font = pygame.font.Font(joystix_monospace, 50)
yourrewards_font = pygame.font.Font(joystix_monospace, 70)
presskey_font = pygame.font.Font(joystix_monospace, 30)

rewards = get_rewards()
reward_counter = 0
reward_text = reward_font.render('Rewards: ' + str(reward_counter), True, (255, 94, 234))

def increase_rewardcounter():
    global reward_counter, reward_text
    reward_counter += 1
    reward_text = reward_font.render('Rewards: ' + str(reward_counter), True, (255, 94, 234))

# Backgrounds
bg_start = pygame.image.load(start_bg).convert()
bg_gameover = pygame.image.load(gameover_bg1).convert()
bg_stop = pygame.image.load(stop_bg).convert()
bg_game = pygame.image.load(game_bg).convert()
bg_congrats = pygame.image.load(congrats_bg).convert()

# Load music
pygame.mixer.music.load(sinnesloschen_beam)

# Play music
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN :

            if event.button == 1 and scene == 1:
                (pos_x, pos_y) = pygame.mouse.get_pos()
                if pos_x > 612 and pos_x < 632+676 and pos_y > 475 and pos_y < 495+112:
                    
                    screen.blit(bg_stop, (0, 0))
                    offset_x = 0
                    offset_y = 0
                    character_jump_count = 0
                    character_is_jumping = False
                    rewards = get_rewards()
                    reward_counter = 0
                    reward_text = reward_font.render('Rewards: ' + str(reward_counter), True, (255, 94, 234))
                    scene = 2
                elif pos_x > 810 and pos_x < 830+280 and pos_y > 675 and pos_y < 695+112:
                    pygame.quit()
                    sys.exit()

            elif event.button == 1 and scene == 3:
                (pos_x, pos_y) = pygame.mouse.get_pos()
                if pos_x > 608 and pos_x < 628+684 and pos_y > 275 and pos_y < 295+162:
                    scene = 2
                elif pos_x > 551 and pos_x < 571+798 and pos_y > 535 and pos_y < 555+114:
                    scene = 1

            elif event.button == 1 and scene == 4:
                (pos_x, pos_y) = pygame.mouse.get_pos()
                if pos_x > 640 and pos_x < 660+212 and pos_y > 620 and pos_y < 640+104:
                    offset_x = 0
                    offset_y = 0
                    character_jump_count = 0
                    character_is_jumping = False
                    rewards = get_rewards()
                    reward_counter = 0
                    reward_text = reward_font.render('Rewards: ' + str(reward_counter), True, (255, 94, 234))
                    scene = 2
                elif pos_x > 1050 and pos_x < 1070+152 and pos_y > 620 and pos_y < 640+104:
                    scene = 1
                    
    # Update game logic here
    if scene == 1:
        screen.blit(bg_start, (0, 0))
        button_start.draw(screen)
        button_quit.draw(screen)
        alpha = 255
        if direction_alpha > 0:
            direction_alpha *= -1

    elif scene == 2:
        screen.blit(bg_game, (0, 0))
        screen.blit(reward_text, (80, 40))

        obstacles_behind.update(offset_x, offset_y)
        obstacles_behind.draw(screen)

        grounds.update(offset_x, offset_y)
        grounds.draw(screen)

        obstacles.update(offset_x, offset_y)
        obstacles.draw(screen)

        portal_entry.update(offset_x, offset_y)
        portal_entry.draw(screen)
        portal_exit.update(offset_x, offset_y)
        portal_exit.draw(screen)

        if character.rect.centerx > portal_exit.rect.centerx-5 and character.rect.centerx < portal_exit.rect.centerx+5:
            if character.rect.centery > portal_exit.rect.y and character.rect.centery < portal_exit.rect.y + portal_exit.rect.height:
                scene = 5

        rewards.update(offset_x, offset_y)
        rewards.draw(screen)

        on_ground = character.check_grounds(grounds)
        if len(on_ground) == 0:
            if not character_is_jumping:
                offset_y -= fall_height
        else:
            if character.rect.bottom != on_ground[0].rect.top + 5:
                offset_y -= abs(character.rect.bottom - (on_ground[0].rect.top + 5))

        if offset_y < -500:
            game_over()

        if character_is_jumping:
            offset_y += jump_height
            character_jump_count += 1
            if character_jump_count > jump_frames:
                character_is_jumping = False
                character_jump_count = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if len(on_ground) > 0 and not character_is_jumping:
                character_is_jumping = True
                character_jump_count = 0
        if keys[pygame.K_ESCAPE]:
            scene = 3
        if keys[pygame.K_a] and offset_x < 220:
            character_direction = 0
            offset_x += 7
        if keys[pygame.K_d]:
            character_direction = 1
            offset_x -= 7
        
        character.check_rewards(rewards, increase_rewardcounter)
        character.check_obstacles(obstacles, obstacles_behind, game_over)
        character.draw(screen, character_direction)

    elif scene == 3:
            screen.blit(bg_stop, (0, 0))
            button_resume.draw(screen)
            button_back.draw(screen)

    elif scene == 4:
        screen.blit(bg_gameover, (0, 0))
        button_yes.draw(screen)
        button_no.draw(screen)

    elif scene == 5:
        screen.blit(bg_congrats, (0, 0))
        yourrewards_text = yourrewards_font.render('Your rewards: ' + str(reward_counter), True, (180, 250, 82))
        screen.blit(yourrewards_text, (520, 450))
        alpha += direction_alpha
        if alpha >= 255 or alpha <= 0:
            direction_alpha *= -1
        presskey_text = presskey_font.render('Press ENTER to continue...', True, (179, 191, 174))
        presskey_text.set_alpha(alpha)
        screen.blit(presskey_text, (650, 600))
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            scene = 1

    # Update display
    pygame.display.flip()
    clock.tick(60)