import pygame


class Block():
    def __init__(self):
        self.block_image = pygame.image.load('images/tetris_block.png')
        self.rect = self.block_image.get_rect()

    def blit_me(self, game_display):
        game_display.blit(self.block_image, (0, 0))


    def new_block(self, game_display):
        self.blit_me(game_display)
