import pygame, random
from enemy import Enemy



class EnemySpawner():
    def __init__(self):
        self.enemy_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 60)

    def update(self):
        self.enemy_group.update()
        for enemy in self.enemy_group:
            if enemy.rect.y >= 720:
                self.enemy_group.remove(enemy)

        if self.spawn_timer == 0:
            self.spawn_enemy()
            self.spawn_timer = random.randrange(30, 60)
        else:
            self.spawn_timer -= 1

    def spawn_enemy(self):
        new_enemy = Enemy()
        self.enemy_group.add(new_enemy)
    
    def clear_enemies(self):
        for enemy in self.enemy_group:
            enemy.kill()