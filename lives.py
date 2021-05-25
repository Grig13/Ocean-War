import pygame, os


class Lives(pygame.sprite.Sprite):
    def __init__(self, num_lives):
        super(Lives, self).__init__()
        self.num_lives = num_lives
        self.width = 80
        self.height = 40
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.image.set_colorkey((0, 0, 0))
        self.player_image = pygame.image.load(os.path.join('Assets', 'fish3.png')).convert_alpha()
        self.player_image = pygame.transform.scale(self.player_image, (self.player_image.get_width(),
                                                                       self.player_image.get_height()))
        self.image.blit(self.player_image, (0, 0))
        self.font_size = 28
        self.font = pygame.font.Font(None, self.font_size)
        self.font_color = (128, 255, 0)
        self.lives_counter = self.font.render(f'X{self.num_lives}', False, self.font_color, False)
        self.image.blit(self.lives_counter, (0, 0))
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        pass

    def decrement_life(self):
        self.num_lives -= 1
        if self.num_lives < 0:
            self.num_lives = 0
        else:
            self.image = pygame.Surface(self.size)
            self.image.set_colorkey((0, 0, 0))
            self.image.blit(self.player_image, (0, 0))
            self.lives_counter = self.font.render(f'X{self.num_lives}', False, self.font_color, False)
            self.image.blit(self.lives_counter, (0, 0))