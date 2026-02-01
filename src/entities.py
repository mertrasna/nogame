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
        self.rect = self.image.get_rect() # creates a super object
        self.rect.center = (x,y) 
        self.vel_y = 0 # Vertical velocity 
        self.speed = stats["speed"]
        self.hp = stats["hp"]
        self.max_hp = stats["hp"] # Store the original total
        self.on_ground = False

        # Animation Variables
        self.action = 0 # 0: Idle, 1: Run, 2: Jump (based on README rows)
        self.update_time = pygame.time.get_ticks() 

        # Combat Variables
        self.attacking = False
        self.attack_type = 0 # for further modification
        self.attack_cooldown = 0 # To prevent spam attacks
        self.hitbox = pygame.Rect(0, 0, 0, 0) # Initialize an empty box
        self.hit_registered = False # Track if this specific swing has landed

    # METHODS
    def apply_physics(self): # reaching 'backpack' with the self argument
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.rect.bottom > FLOOR_Y:
            self.rect.bottom = FLOOR_Y
            self.vel_y = 0
            self.on_ground = True

    def move(self):
        # dx stands for 'delta x'
        dx = 0
        keys = pygame.key.get_pressed() # getting a list of keys currently pressed 

        new_action = self.action

        if not self.attacking:
            new_action = 0

        if self.player_num == 1:
            # Player 1 uses WASD
            if keys[pygame.K_a]: # Move left
                dx = -self.speed
                self.flip = True
                new_action = 1
            elif keys[pygame.K_d]: # Move right
                dx = self.speed
                self.flip = False
                new_action = 1 
            if keys[pygame.K_w] and self.on_ground:
                self.vel_y = -18 # initial upward burst, to go up you must subtract from Y
                self.on_ground = False
            if keys[pygame.K_SPACE] and not self.attacking:
                self.attack()
                return

        elif self.player_num == 2:
            if keys[pygame.K_LEFT]:
                dx = -self.speed
                self.flip = True
                new_action = 1              
            elif keys[pygame.K_RIGHT]:
                dx = self.speed
                self.flip = False
                new_action = 1
            if keys[pygame.K_UP] and self.on_ground:
                self.vel_y = -18
                self.on_ground = False            
            if keys[pygame.K_RETURN] and not self.attacking:
                self.attack()
                return

        if not self.on_ground:
            new_action = 2 # aka jumping

        self.update_action(new_action)
        # Final physical movement
        self.rect.x += dx    

        # Arena boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1280: 
            self.rect.right = 1280    

    def draw(self, screen):
        # Put it on the screen
        screen.blit(self.image, self.rect)

        # Drawing the hitbox as a red outline to test
        if self.attacking:
            pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def update_action(self, new_action):
        # Only reset the animation if the action actually changed
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()     

    def animate(self):
        animation_cooldown = 100 # How fast to animate (lower is faster)

        # Each row in my sheet has 8 frames (4 for right 4 for left)
        # Based on README: Row * 8 gives the start of that row, if we are facing right, we use frames 0-3. If left, 4-7.
        current_row_start = self.action * 8
        side_offset = 4 if self.flip else 0    

        # Real frame count
        actual_index = current_row_start + side_offset + int(self.frame_index)

        # Out of bounds check
        if actual_index < len(self.all_frames):
            self.image = self.all_frames[actual_index]

        # Handle timer
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        # End of animation reset
        if self.frame_index >= 4:
            self.frame_index = 0
            if self.attacking:
                self.attacking = False
                self.action = 0 # After attack, we go back to IDLE pose                

    def attack(self):
        self.attacking = True
        self.hit_registered = False # Reset for the new swing
        self.update_action(3) # Row 3 is attack based on README

    def update(self, target):
        # Every single frame (1/60th of a second), do these:
        self.move() 
        self.apply_physics()  
        self.animate()

        # Hitbox calculation
        if self.attacking:
            h_width = 70
            h_height = 50
            # Center the hitbox vertically on the character
            y_pos = self.rect.centery - (h_height // 2)

            if self.flip:
                self.hitbox = pygame.Rect(self.rect.left - h_width, y_pos, h_width, h_height)
            else:
                self.hitbox = pygame.Rect(self.rect.right, y_pos, h_width, h_height)

        # The hit detection
        if not self.hit_registered:
            if self.hitbox.colliderect(target.rect):
                print(f"{target.name} was hit!")
                target.hp -= 10
                self.hit_registered = True                 