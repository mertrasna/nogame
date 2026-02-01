import pygame

def draw_health_bar(screen, hp, max_hp, x, y, flip=False):
    # health bar constants
    BAR_WIDTH = 350
    BAR_HEIGHT = 15

    # Ratio based health depending on character's health points
    health_ratio = max(0, hp)/ max_hp

    # 2. Draw a Dark "Tray" (The background housing)
    # This makes the UI feel solid
    pygame.draw.rect(screen, (40, 40, 40), (x - 2, y - 2, BAR_WIDTH + 4, BAR_HEIGHT + 4))
    
    # 3. Draw the Red (Damage layer)
    pygame.draw.rect(screen, (150, 0, 0), (x, y, BAR_WIDTH, BAR_HEIGHT))
    
    # 4. Draw the Green (Health layer)
    # Pro Tip: Use a "Modern Green" like (46, 204, 113)
    current_health_width = BAR_WIDTH * health_ratio
    
    # If the bar is on the right (Merlin), we want it to shrink toward the right
    if flip:
        # Drawing from the right side
        pygame.draw.rect(screen, (46, 204, 113), (x + (BAR_WIDTH - current_health_width), y, current_health_width, BAR_HEIGHT))
    else:
        pygame.draw.rect(screen, (46, 204, 113), (x, y, current_health_width, BAR_HEIGHT))

    # 5. Add a slim white highlight line on top for a "glass" effect
    pygame.draw.line(screen, (255, 255, 255), (x, y), (x + current_health_width, y), 1)