from settings_for_tetris import Settings
from settings_for_tetris import Color
from ui import UI
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

        self.ui = UI(self.display_width, self.display_height, self.display)
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

        # Check For Events

    def main(self):
        # Check for events
        while True:
            self.ui.title_screen()
            self.check_events()
            pygame.display.update()


game = Game()
game.main()
