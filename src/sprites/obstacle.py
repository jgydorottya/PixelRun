import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image_path, moving=False, to_x=None, to_y=None, speed=1, rotating=False):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = 0
        self.original_image = self.image.copy()
        self.rotating = rotating
        self.moving = moving
        if moving == True:
            step_x, step_y = (to_x - x)/speed, (to_y -y)/speed
            keyframes = [(0, 0) for _ in range(speed+1)]
            keyframes[0] = (x, y)
            for i in range(1, speed+1):
                keyframes[i] = (x + i*step_x, y + i*step_y)
            self.keyframes = keyframes
            self.speed = speed
            self.current_frame = 0
            self.direction = 1

    def update(self, offset_x, offset_y):
        if self.moving:
            if self.current_frame == self.speed:
                self.direction = -1
            elif self.current_frame == 0:
                self.direction = 1

            self.rect.x = self.keyframes[self.current_frame][0] + offset_x
            self.rect.y = self.keyframes[self.current_frame][1] + offset_y
            self.current_frame += self.direction

        else:
            self.rect.x = self.x + offset_x
            self.rect.y = self.y + offset_y

        if self.rotating:
            self.rotation -= 3
            self.rotation %= 360

            self.image = self.original_image.copy()
            rotated_image = pygame.transform.rotate(self.image, self.rotation)
            new_rect = rotated_image.get_rect(center = self.image.get_rect(center = (self.x + offset_x, self.y + offset_y)).center)

            self.image = rotated_image
            self.rect = new_rect

            self.rect.width = self.width
            self.rect.height = self.height

    def draw(self, screen):
        screen.blit(self.image, self.rect)