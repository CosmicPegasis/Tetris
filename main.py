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
        self.block_moving_x = 0
        self.block_speed_x = False

        # Init Next Block

        # Set Score To Zero

    def check_events(self):
        # Check For Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.block_speed_x = 10
                    self.block_moving_x = True

                self.block_moving_x = False

                if event.key == pygame.K_LEFT:
                    self.block_speed_x = -10
                    self.block_moving_x = True

                self.block_moving_x = False

    def main(self):
        # Check for events
        while True:
            self.ui.game_ui()
            self.check_events()
            self.block.display_block(self.display)
            self.block.move_block(
                self.ui.separator1_pos_x,
                self.block_moving_x,
                self.block_speed_x)
            pygame.display.flip()
            self.block_moving_x = False


game = Game()
game.main()
