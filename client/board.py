"""
Represents the board object for the game
"""
import pygame

class Board(object):
    """
    docstring
    """
    ROWS = COLS = 720
    COLORS = {
        0: (255,255,255),
        1: (0,0,0),
        2: (255,0,0),
        3: (0,255,0),
        4: (0,0,255),
        5: (255,255,0),
        6: (255,140,0),
        7: (165,42,42),
        8: (128,0,128)
    }
    def __init__(self, x, y):
        """
        docstring
        """
        self.x = x
        self.y = y
        self.WIDTH = 720
        self.HEIGHT = 720
        self.compressed_board = []
        self.boar = self.create_board()

    def create_board(self):
        """
        docstring
        """
        return [[(255,255,255) for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def translate_board(self):
        """
        docstring
        """
        for y, _ in enumerate(self.compressed_board):
            for x, col in enumerate(self.compressed_board[y]):
                self.boar[y][x] = self.COLORS[col]

    def draw(self, win):
        """
        docstring
        """
        for y, _ in enumerate(self.compressed_board):
            for x, col in enumerate(self.compressed_board[y]):
                pygame.draw.rect(win, col, (self.x + x, self.y + y, 1, 1), 0)

    def click(self, x, y):
        """
        None if not in board, otherwise return place clicked on
        in terms of row and col
        :x: float
        :y: float
        :return: (int, int) or None
        """
        row = int(x - self.x)
        col = int(y - self.y)

        if 0 <= row < self.ROWS and 0 < col <= self.COLS:
            return row, col
        return None

    def update(self, x, y, color):
        """
        docstring
        """
        self.boar[y][x] = color

    def clear(self):
        """
        docstring
        """
        self.boar = self.create_board()
