import pygame, os


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self.value = 0
        self.color = (128, 255, 0)
        self.font_size = 28
        self.font = pygame.font.Font(None, self.font_size)
        self.x_pad = 990
        self.y_pad = 25
        self.image = self.font.render(str(f'SCORE: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = 1280- self.rect.width - self.x_pad
        self.rect.y = 720 - self.rect.height - self.y_pad

    def update(self):
        pass

    def update_score(self, value):
        self.value += value
        self.image = self.font.render(str(f'SCORE: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = 1280- self.rect.width - self.x_pad
        self.rect.y = 720 - self.rect.height - self.y_pad

    def decrease_score(self, value):
        self.value -= value
        if self.value <= 0:
            self.value = 0
        self.image = self.font.render(str(f'SCORE: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = 1280- self.rect.width - self.x_pad
        self.rect.y = 720 - self.rect.height - self.y_pad