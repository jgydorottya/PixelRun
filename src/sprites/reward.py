import pygame

class Reward(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y

    def update(self, offset_x, offset_y):
        self.rect.x = self.x + offset_x
        self.rect.y = self.y + offset_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)