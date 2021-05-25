import pygame, os
from bullet import Bullet
from worm import Worm
from hud import HUD

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load(os.path.join('Assets', 'fish3.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 640
        self.rect.y = 720 - self.rect.height
        self.max_hp = 3
        self.hp = self.max_hp
        self.lives = 3
        self.hud = HUD(self.hp, self.lives)
        self.is_alive = True
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.hud)
        self.bullets = pygame.sprite.Group()
        self.hearts = pygame.sprite.Group()
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 20

    def update(self):
        self.bullets.update()
        self.hearts.update()
        self.hud_group.update()
        for heart in self.hearts:
            if heart.rect.y <= 0:
                self.hearts.remove(heart)
        for bullet in self.bullets:
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        self.rect.x += self.vel_x
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= 1216:
            self.rect.x = 1216
        self.rect.y += self.vel_y
    
    def shoot(self):
        if self.is_alive:
            new_bullet = Bullet()
            new_bullet.rect.x = self.rect.x + (self.rect.width // 2 - 1)
            new_bullet.rect.y = self.rect.y
            self.bullets.add(new_bullet)
    
    def get_hit(self):
        if self.is_alive:
            self.hp -= 1
            self.hud.health_bar.decrease_hp_value()
            if self.hp <= 0:
                self.hp = 0
                self.death()
            #print(f'HP: {self.hp}')

    def death(self):
        self.lives -= 1
        #print(f'LIVES: {self.lives}')
        if self.lives <= 0:
            self.lives = 0
            self.is_alive = False
            self.image = pygame.Surface((0, 0))
        self.hp = self.max_hp
        self.hud.health_bar.reset_health_to_max()
        self.hud.lives.decrement_life()
        self.rect.x = 1280 // 2