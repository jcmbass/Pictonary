"""
Stores interface for button and two concrete button classes
to be used in th UI.
"""
import pygame

class Button(object):
    """
    When button is created this class handles the correct instantiation of all its properties.
    """
    def __init__(self, x, y, width, height, color, border_color=(0,0,0)):
        """
        Instantiate all properties for button.
        :x: float
        :y: float
        :width: int
        :height: int
        :color: (int,int,int)
        :border_color: (int,int,int)
        """
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.border_color = border_color
        self.BORDER_WIDTH = 2

    def draw(self, win):
        """
        Draws the button in its position.
        :win: Win
        :returns: None
        """
        pygame.draw.rect(win, self.border_color, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(win, self.color, (
        self.x + self.BORDER_WIDTH, self.y + self.BORDER_WIDTH, self.width - self.BORDER_WIDTH * 2,
        self.height - self.BORDER_WIDTH * 2), 0)

    def click(self, x, y):
        """
        If user clicked on button return True.
        :param x: float
        :param y: float
        :return: bool
        """
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True  # user clicked button

        return False

class TextButton(Button):
    """
    Inherits from class Button and adds text drawing support.
    """
    def __init__(self, x, y, width, height, color, text, border_color=(0,0,0)):
        """
        Instantiate all properties for button.
        :x: float
        :y: float
        :width: int
        :height: int
        :color: (int,int,int)
        :text: str
        :border_color: (int,int,int)
        """
        super().__init__(x, y, width, height, color, border_color)
        self.text = text
        self.text_font = pygame.font.SysFont("comicsans", 30)

    def change_font_size(self, size):
        """
        Changes font size in programatic form, needed when having to
        update the game in run time.
        :size: int
        :returns: None
        """
        self.text_font = pygame.font.SysFont("comicsans", size)

    def draw(self, win):
        """
        Draws the text inside the button properly.
        :win: Win
        :returns: None
        """
        super().draw(win)
        txt = self.text_font.render(self.text, 1, (0,0,0))
        win.blit(txt, (self.x + self.width/2 - txt.get_width()/2, self.y + self.height/2 - txt.get_height()/2))
