import pygame, os
from health_bar import HealthBar
from heart_icon import HeartIcon
from score import Score
from lives import Lives


class HUD(pygame.sprite.Sprite):
    def __init__(self, hp, num_lives):
        super(HUD, self).__init__()
        self.image = pygame.image.load(os.path.join('Assets', 'hud.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 720 - self.rect.height
        self.vel_x = 0
        self.vel_y = 0
        self.health_bar = HealthBar(hp)
        self.health_bar.rect.x = 13
        self.health_bar.rect.y = 720 - self.health_bar.rect.height - 36
        self.heealth_bar_group = pygame.sprite.Group()
        self.heealth_bar_group.add(self.health_bar)
        self.score = Score()
        self.score_group = pygame.sprite.Group()
        self.score_group.add(self.score)
        self.heart_icon = HeartIcon()
        self.lives = Lives(num_lives)
        self.lives.rect.x = 120
        self.lives.rect.y = 720 - 30
        self.icons_group = pygame.sprite.Group()
        self.icons_group.add(self.heart_icon)
        self.icons_group.add(self.lives)
        

    def update(self):
        self.heealth_bar_group.update()
        self.icons_group.update()
        self.score_group.update()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y