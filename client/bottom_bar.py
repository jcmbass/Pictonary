import pygame
from button import Button, TextButton

class BottomBar(object):

    """Docstring for BottomBar. """

    def __init__(self, x, y, game):
        """TODO: to be defined.

        :x: TODO
        :y: TODO
        """
        self.x = x
        self.y = y
        self.WIDTH = 720
        self.HEIGHT = 100
        self.BORDER_THICKNESS = 5
        self.game = game
        self.clear_button = TextButton(
                self.x + self.WIDTH - 150,
                self.y + 25,
                100,
                50,
                (128,128,128),
                "Clear")
        self.eraser_button = TextButton(
                self.x + self.WIDTH - 300,
                self.y + 25,
                100,
                50,
                (128,128,128),
                "Eraser")

    def draw(self, win):
        """TODO: Docstring for draw.

        :win: TODO
        :returns: TODO

        """
        pygame.draw.rect(
                win, (0,0,0), (
                    self.x,
                    self.y,
                    self.WIDTH,
                    self.HEIGHT),
                self.BORDER_THICKNESS)
        self.clear_button.draw(win)
        self.eraser_button.draw(win)

    def button_events(self, mouse):
        """
        handle all button press events here
        :returns: TODO

        """
        if self.clear_button.click(*mouse):
            print("Pressed clear button")
        if self.eraser_button.click(*mouse):
            print("Pressed eraser button")
