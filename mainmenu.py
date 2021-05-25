import pygame, sys, os
from Game import *
from two_players import *
from options import *


pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720
display_size  = (screen_width, screen_height)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ocean War")
menu_background = pygame.image.load(os.path.join('Assets', 'ocean_wallpaper_game.png'))

black = (0, 0, 0)
red = (255, 0, 0)
light_red = (255,130,83)
blue = (0, 0, 255)
light_yellow = (255,255,51)
green = (0, 255, 0)
orange_red = (255,69,0)
gold = (255,215,0)
mediumseagreen = (60,179,113)
light_green = (144,238,144)


small_font = pygame.font.Font(os.path.join('Assets','Stacylia DEMO.otf'), 20)
medium_font = pygame.font.Font(os.path.join('Assets','Stacylia DEMO.otf'), 50)
large_font = pygame.font.Font(os.path.join('Assets','Stacylia DEMO.otf'), 80)
main_menu_background_music = pygame.mixer.Sound(os.path.join('Assets', 'background_music.mp3'))



def text_objects(text, color, size = "small"):
    if size == "small":
        textSurface = small_font.render(text, True, color)
    if size == "medium":
        textSurface = medium_font.render(text, True, color)
    if size == "large":
        textSurface = large_font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_to_button(message, color, buttonX, buttonY, buttonWidth, buttonHeight, size = "medium"):
    textSurf, textRect = text_objects(message, color, size)
    textRect.center = ((buttonX + (buttonWidth/2)), (buttonY + (buttonHeight/2)))
    screen.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive_color, active_color):
    cur = pygame.mouse.get_pos()
    if x + width >= cur[0] >= x and y + height >= cur[1] >= y:
        pygame.draw.rect(menu_background, active_color, (x, y, width, height))
    else:
        pygame.draw.rect(menu_background, inactive_color, (x, y, width, height))
    text_to_button(text, black, x, y, width, height)

def main_menu():
    click = False
    while True:
        main_menu_background_music.play()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_position = pygame.mouse.get_pos()
       
       
        button1 = pygame.Rect(200, 600, 200, 50)
        button2 = pygame.Rect(500, 600, 200, 50)
        button3 = pygame.Rect(800, 600, 200, 50)
        

        if button1.collidepoint((mouse_x, mouse_y)):
            if click:
                game()
        if button2.collidepoint((mouse_x, mouse_y)):
            if click:
                two_players()
        if button3.collidepoint((mouse_x, mouse_y)):
            if click:
                Options()

        if 200 + 200 >= mouse_position[0] >= 200 and 600 + 50 >= mouse_position[1] >= 600:
            pygame.draw.rect(menu_background, light_red, button1)
        else:
            pygame.draw.rect(menu_background, orange_red, button1)
        if 500 + 200 >= mouse_position[0] >= 500 and 600 + 50 >= mouse_position[1] >= 600:
            pygame.draw.rect(menu_background, light_yellow, button2)
        else:
            pygame.draw.rect(menu_background, gold, button2)
        if 800 + 200 >= mouse_position[0] > 800 and 600 + 50 >= mouse_position[1] >= 600:
            pygame.draw.rect(menu_background,light_green, button3)
        else:
            pygame.draw.rect(menu_background,mediumseagreen, button3)
        
        screen.blit(menu_background,[0, 0])

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True       
        text_to_button("SinglePlayer", black, 200, 600, 200, 50) 
        text_to_button("2 Players", black, 500, 600, 200, 50)
        text_to_button("Controls", black, 800, 600, 200, 50)
        pygame.display.update()
        clock.tick(30)
main_menu() 