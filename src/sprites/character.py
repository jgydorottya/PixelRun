import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.mirrored_image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

    def draw(self, screen, character_direction):
        if character_direction == 1:
            screen.blit(self.image, self.rect)
        else:
            screen.blit(self.mirrored_image, self.rect)

    def check_rewards(self, rewards, increase_rewardcounter):
            if pygame.sprite.spritecollide(self, rewards, True):
                increase_rewardcounter()

    def check_obstacles(self, obstacles, obstacles_behind, game_over):
        if pygame.sprite.spritecollide(self, obstacles, False):
            game_over()
        if pygame.sprite.spritecollide(self, obstacles_behind, False):
            game_over()

    def check_grounds(self, grounds):
        return pygame.sprite.spritecollide(self, grounds, False)