import pygame, os, random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load(os.path.join('Assets', 'enemy.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 1280 - 64)
        self.rect.y = -self.rect.height
        self.hp = 3
        self.point_value = 5
        self.vel_x = 0
        self.vel_y = random.randrange(11, 15)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def get_hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.destroy() 

    def destroy(self):
        self.kill()