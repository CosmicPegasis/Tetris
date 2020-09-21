from settings import Settings
import pygame


# Main Class
class Game():
    def __init__(self):
        self.Settings = Settings()

        # Screen
        self.display = pygame.display.set_mode(self.Settings.screen_dimensions)


    # Score

    # Different Blocks

    # Next Block Display

    # Title Screen and You Lose Screen

    def main(self):
        pygame.display.update()
