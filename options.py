import pygame, os, sys

pygame.init()

screen_width = 1280
screen_height = 720
display_size  = (screen_width, screen_height)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Controls")
options_background = pygame.image.load(os.path.join('Assets', 'options_background.png'))

def Options():
    running = True
    keys_pressed = pygame.key.get_pressed()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if keys_pressed[pygame.K_a]:
                running = False
                pygame.quit()
                sys.exit()
        screen.blit(options_background, (0, 0))
        pygame.display.update()
