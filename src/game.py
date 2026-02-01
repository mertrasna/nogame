import pygame
from src.entities import Fighter
from src.ui import draw_health_bar
from src.settings import SCREEN_HEIGHT, SCREEN_WIDTH, FLOOR_Y

class Game:
    def __init__(self, screen):
        self.screen = screen
        pygame.display.set_caption("Nogame")
        # icon = pygame.image.load('assets/icon.png')
        # pygame.display.set_icon(icon)
        self.game_over = False
        self.winner = None
        self.font = pygame.font.SysFont("Arial", 26, bold=True)
        self.reset() # Setup initial state

    def reset(self):
        self.game_over = False
        self.winner = None

        arthur_stats = {"hp": 100, "speed": 9}
        gawain_stats = {"hp": 150, "speed": 7}

        self.p1 = Fighter(1, 200, FLOOR_Y, "arthurPendragon_", arthur_stats)
        self.p2 = Fighter(2, 1080, FLOOR_Y, "gawain_", gawain_stats)

    def update(self):
        if not self.game_over:
            self.p1.update(self.p2)
            self.p2.update(self.p1)

            # Check win condition
            if self.p1.hp <= 0:
                self.game_over = True
                self.winner = self.p2.name
            elif self.p2.hp <= 0:
                self.game_over = True
                self.winner = self.p1.name

    def draw(self, bg_image):
        self.screen.blit(bg_image, (0,0))
        draw_health_bar(self.screen, self.p1.hp, self.p1.max_hp, 50, 40)
        draw_health_bar(self.screen, self.p2.hp, self.p2.max_hp, 880, 40, flip=True)

        self.p1.draw(self.screen)
        self.p2.draw(self.screen)

        if self.game_over:
            self._draw_victory_screen()

    def _draw_victory_screen(self):
        # Internal helper for drawing the KO message
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(150)
        overlay.fill((0,0,0))
        self.screen.blit(overlay, (0,0)) 

        txt = self.font.render(f"{self.winner.upper()} WINS! Press 'R' to Rematch", True, (255, 215, 0))
        self.screen.blit(txt, (SCREEN_WIDTH//2 - txt.get_width()//2, SCREEN_HEIGHT//2))       

                            

