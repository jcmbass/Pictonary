"""
Represents a player object on the server side
"""

class Player():
    def __init__(self, ip, name):
        """Init the player object

        :ip: str
        :name: str
        """
        self.game = None
        self.ip = ip
        self.name = name
        self.score = 0

    def set_game(self, game):
        """Sets the players game association

        :game: Game
        :returns: None

        """
        self.game = game

    def update_score(self, x):
        """Updates a players score

        :x: int
        :returns: None

        """
        self.score += x

    def guess(self, wrd):
        """Makes a player guess

        :wrd: str
        :returns: bool

        """
        self.game.player_guess(wrd)

    def disconnect(self):
        """Call to disconnect player
        :returns: None

        """
        self.game.player_disconnected(self)

    def get_ip(self):
        """Gets player ip address

        :returns: str

        """
        return self.ip

    def get_name(self):
        """Gets player name
        :returns: str
        """
        return self.name

    def get_score(self):
        """Gets player score
        :returns: int

        """
        return self.score
