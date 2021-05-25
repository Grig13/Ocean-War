import pygame, sys, os, random
from sp_Player import Player
from enemy_spawner import EnemySpawner
from worm_spawner import WormSpawner
from alert_box import AlertBox


pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720
BLACK = (0, 0, 0)

pygame.display.set_caption("Ocean War")
game_background = pygame.image.load(os.path.join('Assets', 'singleplayerwallpaper.png'))
screen = pygame.display.set_mode((screen_width, screen_height))
screen_rect = game_background.get_rect()

player_width, player_height = 64, 64
poison_width, poison_height = 64, 64
thunder_width, thunder_height = 64, 64

menu_background = pygame.image.load(os.path.join('Assets', 'ocean_wallpaper_game.png'))
poison_image = pygame.image.load(os.path.join('Assets', 'poison.png')).convert_alpha()
thunder_image = pygame.image.load(os.path.join('Assets', 'speed.png')).convert_alpha()

click = False

def game():
    player = Player()
    sprite_group = pygame.sprite.Group()
    sprite_group.add(player)
    powerups = pygame.sprite.Group()
    alert_box_group = pygame.sprite.Group()

    enemy_spawner = EnemySpawner()
    worm_spawner = WormSpawner()
    alert_box = AlertBox("GAME OVER")
    running = True
    bg_y = 0
    start_ticks=pygame.time.get_ticks()
    while running:

        # Handle events
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.vel_x = -player.speed
                elif event.key == pygame.K_RIGHT:
                    player.vel_x = player.speed
                elif event.key == pygame.K_SPACE:
                    player.shoot()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.vel_x = 0
                elif event.key == pygame.K_RIGHT:
                    player.vel_x = 0
        
        # Update all the objects
        sprite_group.update()
        enemy_spawner.update()
        worm_spawner.update()
        alert_box.update()
        # Check for collision

        collided = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, True)
        for bullet, enemy in collided.items():
            enemy[0].get_hit()
            player.hud.score.update_score(enemy[0].point_value)

        wormcollided = pygame.sprite.groupcollide(player.bullets, worm_spawner.worm_group, True, True)
        for bullet, hearts in wormcollided.items():
            hearts[0].get_hit()

        collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, True)
        for player, enemy in collided.items():
            enemy[0].hp = 0
            enemy[0].get_hit()
            player.get_hit()

        #wormcollide = pygame.sprite.groupcollide(sprite_group, worm_spawner.worm_group, False, True)
        #for player in collided.items():
            #player.hp += 1


        # Check for GO

        if not player.is_alive:
            enemy_spawner.clear_enemies()
            alert_box_group.add(alert_box)
        # Render the display
        rel_y = bg_y % screen_rect.height
        screen.blit(game_background, (0, rel_y - screen_rect.height))
        if rel_y < screen_height:
            screen.blit(game_background, (0, rel_y))
        bg_y += 5
        player.bullets.draw(screen)
        
        enemy_spawner.enemy_group.draw(screen)
        
        if player.is_alive:
            seconds=(pygame.time.get_ticks()-start_ticks)/1000 
            if seconds > 25:
                seconds = 0
                player.hearts.draw(screen)
                worm_spawner.worm_group.draw(screen)
        player.hud_group.draw(screen)
        player.hud.heealth_bar_group.draw(screen)
        sprite_group.draw(screen)
        player.hud.icons_group.draw(screen)
        player.hud.score_group.draw(screen)
        alert_box_group.draw(screen)
        pygame.display.update()
        clock.tick(30)
