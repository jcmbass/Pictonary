"""
Handles operatins related to game and connections
between, player, board chat and round
"""
from board import Board
from round import Round
import random

class Game(object):

    """Docstring for Game. """

    def __init__(self, id, players):
        """init the game! once player threshold is met.

        :id: int
        :players: Player[]

        """
        self.id = id
        self.players = []
        self.words_used = []
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0
        self.round_count = 1
        self.start_new_round()

    def start_new_round(self):
        """Starts a new round with a new word.
        :returns: None

        """
        try:
            round_word = self.get_word()
            self.round = Round(round_word, self.players[self.player_draw_ind], self)
            self.player_draw_ind += 1

            if self.player_draw_ind >= len(self.players):
                self.round_ended()
                self.end_game()
            
            self.round_count += 1
        except:
            self.end_game()

    def player_guess(self, player, guess):
        """Make the player guess the word.
        :player: Player
        :guess: str
        :returns: bool

        """
        return self.round.guess(player, guess)

    def player_disconnected(self, player):
        """Call to clean up objects when player disconnects.

        :player: Player
        :raises: Exception()

        """

        # TODO check this later
        if player in self.players:
            player_ind = self.players.index(player)
            if player_ind >= self.player_draw_ind:
                self.player_draw_ind -= 1
            self.players.remove(player)
            self.round.player_left(player)
        else:
            raise Exception("Player not in game")

        if len(self.players) <= 2:
            self.end_game()

    def get_player_scores(self):
        """Give a dict of player scores
        :returns: dict
        """
        scores = {player:player.get_score() for player in self.players}
        return scores

    def skip(self):
        """Increments the round skips, if skips are greater than
        threshold, starts new round.
        :returns: bool

        """
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()
                return True
            return False
        else:
            raise Exception("No round started yet!")

    def round_ended(self):
        """If the round ends call this.
        :returns: None

        """

        self.start_new_round()
        self.board.clear()

    def update_board(self, x, y, color):
        """Calls update method on board.
        :x: int
        :y: int
        :color: 0-8
        :returns: None

        """
        if not self.board:
            raise Exception("No board created")
        self.board.update(x,y,color)

    def end_game(self):
        """Clears the list of all players when the games ends
        :returns: None

        """
        print(f"[GAME] {self.id} ended")
        for player in self.players:
            player.game = None

    def get_word(self):
        """gives a word that has not yet been used
        :returns: str

        """
        with open("words.txt", "r") as f:
            words = []
            for line in f:
                wrd = line.strip()
                if wrd not in self.words_used:
                    words.append(wrd)

            self.words_used.append(wrd)
            r = random.randint(0, len(words))
            return words[r].strip()
