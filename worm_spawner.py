import pygame, random
from worm import Worm


class WormSpawner():
    def __init__(self):
        self.worm_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 60)

    def update(self):
        self.worm_group.update()
        for worm in self.worm_group:
            if worm.rect.y >= 720:
                self.worm_group.remove(worm)
        if self.spawn_timer == 0:
            self.spawn_worm()
            self.spawn_timer = random.randrange(30, 60)
        else:
            self.spawn_timer -= 1

    def spawn_worm(self):
        new_worm = Worm()
        self.worm_group.add(new_worm)