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

        # Animation Variables
        self.action = 0 # 0: Idle, 1: Run, 2: Jump (based on README rows)
        self.update_time = pygame.time.get_ticks() 

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
        # Put it on the screen
        screen.blit(self.image, self.rect)

    def animate(self):
        animation_cooldown = 100 # How fast to animate (lower is faster)

        # Each row in my sheet has 8 frames (4 for right 4 for left)
        # Based on README: Row * 8 gives the start of that row, if we are facing right, we use frames 0-3. If left, 4-7.
        current_row_start = self.action * 8
        side_offset = 4 if self.flip else 0    

        # Calculate the exact frame index in the big list, we use % 4 to make sure it loops.
        actual_index = current_row_start + side_offset + (int(self.frame_index) % 4)
        self.image = self.all_frames[actual_index]

        # Check if enough time has passed to change frames
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

    def update(self):
        # Every single frame (1/60th of a second), do these:
        self.move() 
        self.apply_physics()  
        self.animate()
