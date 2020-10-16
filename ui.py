import pygame
from settings_for_tetris import Color


class UI():
    def __init__(self, display_width, display_height, display):
        self.display_width = display_width
        self.display_height = display_height
        self.display = display
        self.color = Color()

    # Inits both separators
    def game_ui(self):
        self.separator_1()
        self.separator_2()

    # Vertical separator
    def separator_1(self):
        self.separator1_pos_x = int(2 * self.display_width/3 - 13)
        separator1_length = self.display_height

        pygame.draw.rect(
            self.display, self.color.white,
            (self.separator1_pos_x, 0, 2, separator1_length))

    # Horizontal Seperator
    def separator_2(self):
        separator2_pos_x = self.separator1_pos_x
        separator2_pos_y = int(self.display_height/2)
        separator2_width = int(self.display_width - self.separator1_pos_x)

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

    # Title Screen
    def title_screen(self):
        title_text = 'Welcome To Tetris'
        color = self.color.green

        self.show_text(
            title_text,
            color,
            self.display_width / 2,
            self.display_height / 2 - 100,
            font_size=40)

        title_sub_text = 'Press P To Play Or Q To Exit'

        self.show_text(
            title_sub_text,
            color,
            self.display_width / 2,
            self.display_height / 2,
            font_size=20)

    # You Lose Screen
    def you_lose_screen(self):
        lose_text = 'You Lost'
        color = self.color.green

        self.show_text(
            lose_text,
            color,
            self.display_width / 2,
            self.display_height / 2 - 100,
            font_size=40)

        lose_sub_text = 'Press P To Play Again Or Q To Exit'

        self.show_text(
            lose_sub_text,
            color,
            self.display_width / 2,
            self.display_height / 2,
            font_size=20)

    def show_text(self, text, color, pos_x, pos_y, font_size=40):
        font = pygame.font.SysFont('Source Code Pro', font_size)
        font_surface = font.render(text, 0, color)

        font_width = font_surface.get_rect().width
        font_height = font_surface.get_rect().height

        self.display.blit(
            font_surface,
            (pos_x - font_width / 2,
             pos_y - font_height / 2))
        # Text Display
