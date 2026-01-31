# Pygame works with pixels, not math-based vectors
import pygame
import sys 
from src.settings import * # module import(global) for speed, from src import settigns later
from src.entities import Fighter

def main():

    pygame.init()
    # Creating the window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Nogame")
    clock = pygame.time.Clock()

    arthur_stats = {"hp": 100, "speed": 7}
    merlin_stats = {"hp": 80, "speed": 9}
    p1 = Fighter(1, 200, FLOOR_Y, "arthurPendragon_", arthur_stats)
    p2 = Fighter(2, 1000, FLOOR_Y, "merlin_", merlin_stats)

    # -- THE GAME LOOP --
    running = True
    # Background configs
    bg_image = pygame.image.load("assets/backgrounds/game_background_1.png").convert() 
    bg_image = pygame.transform.scale(bg_image,(SCREEN_WIDTH, SCREEN_HEIGHT))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


        # --- THE HEARTBEAT ---
        # This runs move() and apply_physics() 60 times a second
        p1.update()
        p2.update()
        # drawing the background at (0,0) - the top left corner
        screen.blit(bg_image, (0,0))
        
        # Draw the character at their new position
        p1.draw(screen)
        p2.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()