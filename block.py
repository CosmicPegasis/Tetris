import pygame


class Block():
    def __init__(self):
        self.block_image = pygame.image.load('images/tetris_block.png')
        self.rect = self.block_image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def blit_me(self, game_display):
        # Draw them on screen
        game_display.blit(self.block_image, (self.rect.x, self.rect.y))

    def display_block(self, game_display):
        self.blit_me(game_display)

    def move_block(self, play_field_length, block_moving_x, block_speed_x):
        # Block Movement
        while block_moving_x:
            # if self.rect.x >= 0 and self.rect.x <= play_field_length:
            self.rect.x += block_speed_x

    # Different Blocks
        # Set Block
        # Block Randomiser
