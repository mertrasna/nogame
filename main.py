# Pygame works with pixels, not math-based vectors
import pygame
import sys 
from src.settings import * # module import(global) for speed, from src import settigns later
from src.entities import Fighter
from src.ui import draw_health_bar
from src.game import Game
import random

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    bg_image = pygame.image.load("assets/backgrounds/game_background_3.png").convert_alpha()
    bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game Manager (game.py)
    game_manager = Game(screen)

    # -- THE GAME LOOP --
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_r and game_manager.game_over:
                    game_manager.reset()    

        game_manager.update()
        game_manager.draw(bg_image)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()