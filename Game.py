import pygame
import sys

pygame.init()

clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ocean War")

menu_background = pygame.image.load('ocean_wallpaper(unfinished).png')

click = False



def game():
    running = True
    screen.fill((0,0,0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    running = False
        pygame.display.update()
        clock.tick(30)
