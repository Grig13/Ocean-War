import pygame, sys, os, random
from pygame.locals import *



pygame.init()
pygame.font.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

RED = (255, 0, 0)
GREEN = (0, 255, 0)

border = pygame.Rect(screen_width // 2 - 5, 0, 10, screen_height)

max_bullets = 3
bullet_velocity = 20
red_bullets = []
green_bullets = []



clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)


red_hit = pygame.USEREVENT + 1  #creating a custom event. +1 and +2 so they can be different. adding the numbers
#in order to add unicity.
green_hit = pygame.USEREVENT + 2



first_player_width, first_player_height = 64, 64
second_player_width, second_player_height = 64, 64

first_player = pygame.image.load(os.path.join('Assets', 'fish1.png'))
second_player = pygame.image.load(os.path.join('Assets', 'fish2.png'))
two_players_background = pygame.image.load(os.path.join('Assets', 'two_players_background.png'))
health_font = pygame.font.SysFont('comicsans', 40)
winner_font = pygame.font.SysFont('comicsans', 100)


red = pygame.Rect(200, 360, first_player_width, first_player_height)
green = pygame.Rect(1080, 360, second_player_width, second_player_height)

red_velocity = 15
green_velocity = 15


def draw_screen(red_bullets, green_bullets, red_health, green_health):
    
    screen.blit(two_players_background, (0, 0))
    pygame.draw.rect(screen, black, border)


    red_health_text = health_font.render('Health : ' + str(red_health), 1, white)
    green_health_text = health_font.render('Health : ' + str(green_health), 1, white)
    screen.blit(red_health_text, (screen_width - red_health_text.get_width() - 10, 10))
    screen.blit(green_health_text, (10, 10))

    screen.blit(first_player, (red.x, red.y))
    screen.blit(second_player, (green.x, green.y))
    for bullet in red_bullets:
        pygame.draw.rect(screen, RED, bullet)
    for bullet in green_bullets:
        pygame.draw.rect(screen, GREEN, bullet)
    
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

def handle_bullets(red_bullets, green_bullets, red, green):
    for bullet in red_bullets:
        bullet.x += bullet_velocity
        if green.colliderect(bullet):
            pygame.event.post(pygame.event.Event(green_hit))
            red_bullets.remove(bullet)
        elif bullet.x > screen_width:
            red_bullets.remove(bullet)

    for bullet in green_bullets:
        bullet.x -= bullet_velocity
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            green_bullets.remove(bullet)
        elif bullet.x < 0:
            green_bullets.remove(bullet)

def draw_winner(text):
    draw_text = winner_font.render(text, 1, white)
    screen.blit(draw_text, (screen_width / 2 - draw_text.get_width() / 
                            2, screen_height / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000) # <- delay time is 1000 * how many seconds you want to delay it with.



def two_players():
    red_health = 10
    green_health = 10
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(green_bullets) < max_bullets:
                    bullet = pygame.Rect(green.x, green.y + green.height // 2 - 2, 10, 5)
                    green_bullets.append(bullet)

            if event.type == red_hit:
                green_health -= 1
            if event.type == green_hit:
                red_health -= 1

        winner_text = ''
        if red_health <= 0:
            winner_text = 'Red fish wins!'
        if green_health <= 0:
            winner_text = 'Green fish wins!'
        if winner_text != '': 
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        first_player_movement(keys_pressed, red)
        second_player_movement(keys_pressed, green)
        handle_bullets(red_bullets, green_bullets, red, green)
        draw_screen(red_bullets, green_bullets, red_health, green_health)
        
        clock.tick(30)