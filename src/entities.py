import pygame
from src.settings import GRAVITY, FLOOR_Y
from src.utils import load_spritesheet

class Fighter(pygame.sprite.Sprite): # inherit powers of pygame.sprite.Sprite
    # 'self' keyword for pinning variables to that specific object
    def __init__(self, player_num, x, y, name, stats): # For things happens ONCE
        # Initialize the parent Sprite class
        super().__init__() # super() refers to the "superclass"

        self.player_num = player_num # Who is controlling the object
        self.name = name

        # Loading the art with slicer
        sprite_path = f"assets/sprites/{self.name}.png"
        self.all_frames = load_spritesheet(sprite_path, 32, 32, 4) # Scale of 4 makes our char 128px tall

        # Starting visuals
        self.frame_index = 0 # pointer to a specific photo
        self.image = self.all_frames[self.frame_index]
        self.flip = False if player_num == 1 else True

        # Physics & Stats
        self.rect = self.image.get_rect()
        self.rect.center = (x,y) 
        self.vel_y = 0 # Vertical velocity 
        self.speed = stats["speed"]
        self.hp = stats["hp"]
        self.on_ground = False

    # METHODS
    def apply_physics(self): # reaching 'backpack' with the self argument
        self.vel_y = GRAVITY
        self.rect.y += self.vel_y

        if self.rect.bottom > FLOOR_Y:
            self.rect.bottom = FLOOR_Y
            self.vel_y = 0
            self.on_ground = True

    def move(self):
        # dx stands for 'delta x'
        dx = 0

        keys = pygame.key.get_pressed() # getting a list of keys currently pressed 

        if self.player_num == 1:
            # Player 1 uses WASD
            if keys[pygame.K_a]: # Move left
                dx = -self.speed
                self.flip = True
            if keys[pygame.K_d]: # Move right
                dx = self.speed
                self.flip = False 

            if keys[pygame.K_w] and self.on_ground:
                self.vel_y = -18 # initial upward burst, to go up you must subtract from Y
                self.on_ground = False           

        self.rect.x += dx

    def draw(self, screen):
        # Handling direction, if self.flip is true, it mirrors the image horizontally
        img_to_draw = pygame.transform.flip(self.image, self.flip, False)

        # Put it on the screen
        screen.blit(img_to_draw, self.rect)
            

    def update(self):
        # Every single frame (1/60th of a second), do these:
        self.move() 
        self.apply_physics()  
