"""
Stores the state of the drawing board.
"""

class Board(object):

    """Docstring for Board."""
    ROWS = COLS = 720

    def __init__(self):
        """Init the board by creating empty board (all white pixels)"""
        self.data = self._create_empty_board()

    def update(self, x, y, color):
        """
        Updates a singular pizel of the board.
        :x: int
        :y: int
        :color: (int,int,int)
        :returns: None
        """

        self.data[y][x] = color

    def clear(self):
        """Clears board to all white.
        :returns: None

        """
        self.data = self._create_empty_board()

    def _create_empty_board(self):
        """Creates an empty board (all white)
        :returns: TODO

        """
        return [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def fill(self, x, y):
        """Fills in a specific shape or area using recursion.
        :x: int
        :y: int
        :returns: None

        """
        pass

    def get_board(self):
        """Gets the data of the board.
        :returns: (int,int,int)

        """
        return self.data
