from settings_for_tetris import Settings
from settings_for_tetris import Color
from ui import UI
from block import Block
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
        # TODO Add SCALED once pygame updates to 2.0

        pygame.display.set_caption('Tetris')

        self.ui = UI(self.display_width, self.display_height, self.display)
        # Init new block
        self.block = Block()

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
            self.ui.game_ui()
            self.check_events()
            self.block.new_block(self.display)
            pygame.display.flip()


game = Game()
game.main()
