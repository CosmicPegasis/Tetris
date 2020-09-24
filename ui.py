import pygame


class UI():
    def __init__(self, display_width, display_height, display):
        self.display_width = display_width
        self.display_height = display_height
        self.display = display

    def game_ui(self):
        self.separator_1()
        self.separator_2()

    def separator_1(self):
        self.separator1_pos_x = int(2 * self.display_width/3)
        separator1_length = self.display_height

        pygame.draw.rect(
            self.display, [255, 255, 255],
            (self.separator1_pos_x, 0, 2, separator1_length))

    def separator_2(self):
        separator2_pos_x = self.separator1_pos_x
        separator2_pos_y = int(self.display_height/2)
        separator2_width = int(self.display_width - self.separator1_pos_x)

        pygame.draw.rect(
            self.display,
            [255, 255, 255],
            (separator2_pos_x,
             separator2_pos_y,
             separator2_width,
             2))
        # Score
        # Update with every block set

        # Next Block Display

        # Title Screen and you Lose Screen
        # Text Display
