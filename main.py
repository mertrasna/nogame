# Pygame works with pixels, not math-based vectors
import pygame
import sys 
from src.settings import * # module import(global) for speed, from src import settigns later

def main():

    pygame.init()

    # Creating the window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Nogame")

    clock = pygame.time.Clock()

    # Temporary "Rect" representing our player
    player_rect = pygame.Rect(100, FLOOR_Y - 100, 50, 100)

    # -- THE GAME LOOP --
    running = True
    while running:
        # Check for events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Draw everything
        screen.fill(BLACK) # Clear screen first

        # Temp player
        pygame.draw.rect(screen, RED, player_rect)

        # Update the display
        pygame.display.flip()

        # Keep the game running at exactly 60 FPS
        clock.tick(FPS)

    pygame.quit() # shut downs the game engine
    sys.exit() # tells this python program is finished, close it and give memory back 


# Safety switch
if __name__ == "__main__":
    main()    