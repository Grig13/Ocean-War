import pygame, os


class HeartIcon(pygame.sprite.Sprite):
    def __init__(self):
        super(HeartIcon, self).__init__()
        self.img_heart_01 = pygame.image.load(os.path.join('Assets', 'heart1.png')).convert_alpha()
        self.img_heart_02 = pygame.image.load(os.path.join('Assets', 'heart2.png')).convert_alpha()
        self.img_heart_03 = pygame.image.load(os.path.join('Assets', 'heart3.png')).convert_alpha()
        self.img_heart_04 = pygame.image.load(os.path.join('Assets', 'heart4.png')).convert_alpha()
        self.img_heart_05 = pygame.image.load(os.path.join('Assets', 'heart5.png')).convert_alpha()
        self.anim_list = [self.img_heart_01,
                          self.img_heart_02,
                          self.img_heart_03,
                          self.img_heart_04,
                          self.img_heart_05]
        self.anim_index = 0
        self.max_index = len(self.anim_list) - 1
        self.max_frame_duration = 3
        self.frame_duration = self.max_frame_duration
        self.image = self.anim_list[self.anim_index]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 720 - self.rect.height - 25

    def update(self):
        if self.frame_duration == 0:
            self.anim_index += 1
            if self.anim_index > self.max_index:
                self.anim_index = 0
            self.image = self.anim_list[self.anim_index]
            self.frame_duration = self.max_frame_duration
        self.frame_duration -= 1