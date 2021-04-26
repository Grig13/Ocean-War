import pygame, sys

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

border = pygame.Rect(screen_width/2 - 5, 0, 10, screen_height)

clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)

first_player_width, first_player_height = 64, 64
second_player_width, second_player_height = 64, 64

first_player = pygame.image.load('fish1.png')
second_player = pygame.image.load('fish2.png')

red = pygame.Rect(200, 360, first_player_width, first_player_height)
green = pygame.Rect(1080, 360, second_player_width, second_player_height)
red_velocity = 10
green_velocity = 10

def draw_screen():
    screen.fill((black))
    pygame.draw.rect(screen, white, border)
    screen.blit(first_player, (red.x, red.y))
    screen.blit(second_player, (green.x, green.y))
    pygame.display.update()


def first_player_movement(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.x - red_velocity > 0:
        red.x -= red_velocity
    if keys_pressed[pygame.K_d] and red.x + red_velocity + red.width < border.x:
        red.x += red_velocity
    if keys_pressed[pygame.K_w] and red.y - red_velocity > 0:
        red.y -= red_velocity
    if keys_pressed[pygame.K_s] and red.y + red_velocity + red.height < screen_height:
        red.y += red_velocity


def second_player_movement(keys_pressed, green):
    if keys_pressed[pygame.K_LEFT] and green.x - green_velocity > border.x + border.width:
        green.x -= green_velocity
    if keys_pressed[pygame.K_RIGHT] and green.x - green_velocity + green.width < screen_width - 20:
        green.x += green_velocity
    if keys_pressed[pygame.K_UP] and green.y - green_velocity > 0:
        green.y -= green_velocity
    if keys_pressed[pygame.K_DOWN] and green.y + green_velocity + green.height < screen_height:
        green.y += green_velocity


def two_players():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()   
        keys_pressed = pygame.key.get_pressed()
        first_player_movement(keys_pressed, red)
        second_player_movement(keys_pressed, green)
        draw_screen()
        clock.tick(30)
