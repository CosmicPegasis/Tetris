from settings_for_tetris import Settings
from settings_for_tetris import Color
import pygame


# Main Class
class Game():
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.color = Color()

        self.display = pygame.display.set_mode(self.settings.screen_dimensions)
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
    # def ui(self):
        # Separator Lines

        # Score
        # Update with every block set

        # Next Block Display

        # Title Screen and you Lose Screen
        # Text Display
        # Check For Events

    def main(self):
        # Check for events
        while True:
            self.check_events()
            pygame.display.update()


game = Game()
game.main()
