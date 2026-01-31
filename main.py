# Pygame works with pixels, not math-based vectors
import pygame
import sys 
from src.settings import * # module import(global) for speed, from src import settigns later
from src.entities import Fighter

def main():

    pygame.init()
    # Creating the window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Nogame")
    clock = pygame.time.Clock()

    arthur_stats = {"hp": 100, "speed": 7}
    p1 = Fighter(1,200, FLOOR_Y, "arthurPendragon_", arthur_stats)

    # -- THE GAME LOOP --
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- THE HEARTBEAT ---
        # This runs move() and apply_physics() 60 times a second
        p1.update()

        # --- THE CANVAS ---
        screen.fill(BLACK) # Clear the old frame
        
        # Draw the character at their new position
        p1.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()