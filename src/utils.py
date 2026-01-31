# for sprite-handling
import pygame

def load_spritesheet(filename, frame_width, frame_height, scale):
    # Load the image and ensure transparency is handled
    sheet = pygame.image.load(filename).convert_alpha()

    sprites= [] # 2D image or animation that represents an object in game (like a player, enemy, etc.)
    sheet_width, sheet_height = sheet.get_size()

    rows = sheet_width // frame_height
    cols = sheet_height // frame_width

    # Loop through the grid and cut on the squares
    for r in range(rows):
        for c in range(cols):
            # Create a blank transparent surface for one frame
            image = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA) # specific flag that tells "this surface needs to support transparency"

            # Draw the specific chunk onto our small surface
            # Surface to draw on, where to draw and area to take from the source
            image.blit(sheet, (0,0), (c * frame_width, r * frame_height, frame_width, frame_height))

            # Scale it up so that it's visible on HD screen
            image = pygame.transform.scale(image, (frame_width * scale, frame_height  * scale))

            sprites.append(image)

    return sprites        