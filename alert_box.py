import pygame

class AlertBox(pygame.sprite.Sprite):
    def __init__(self, message):
        super(AlertBox, self).__init__()
        self.font = pygame.font.Font(None, 70)
        self.color = (255, 0, 0)
        self.message = message
        self.image = self.font.render(self.message, 0, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = 1280 // 2 - self.rect.width // 2
        self.rect.y = 720 // 2 - self.rect.height // 2
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y