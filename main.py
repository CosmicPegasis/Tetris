from settings_for_tetris import Settings
from settings_for_tetris import Color
import pygame


# Main Class
class Game():
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.color = Color()
        self.display_width = self.settings.screen_dimensions[0]
        self.display_height = self.settings.screen_dimensions[1]

        self.display = pygame.display.set_mode(
            (self.display_width, self.display_height))
        # Init new block

        # Init Next Block

        # Set Score To Zero

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    # Different Blocks
        # Import different block images
        # Draw them on screen
        # Block Movement
        # Set Block
        # Block Randomiser

    # UI
    def ui(self):
        # Separator Lines
        # Separator 1
        separator1_pos_x = int(2 * self.display_width/3)
        separator1_length = self.display_height

        pygame.draw.rect(
            self.display, self.color.white,
            (separator1_pos_x, 0, 2, separator1_length))

        separator2_pos_x = separator1_pos_x
        separator2_pos_y = int(self.display_height/2)
        separator2_width = int(self.display_width - separator1_pos_x)

        pygame.draw.rect(
            self.display,
            self.color.white,
            (separator2_pos_x,
             separator2_pos_y,
             separator2_width,
             2))

        # Score
        # Update with every block set

        # Next Block Display

        # Title Screen and you Lose Screen
        # Text Display
        # Check For Events

    def show_text(self, text, pos):
        font = pygame.font.SysFont('Source Code Pro', 20)
        font_surface = font.render(text, pos, antialias=1)
        self.display.blit(font_surface, (0, 0))

    def main(self):
        # Check for events
        while True:
            self.ui()
            self.check_events()
            pygame.display.update()


game = Game()
game.main()
