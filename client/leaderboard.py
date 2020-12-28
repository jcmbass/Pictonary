"""
Represents the leaderboard object for the client side of the game.
"""
import pygame

class Leaderboard(object):
    """
    Leaderboard shows a list of all players in game and displays scores in a format
    that is readable and clear.
    """
    def __init__(self, x, y):
        """
        Instantiate the leaderboar object.
        """
        self.x = x
        self.y = y
        self.WIDTH = 200
        self.HEIGHT_ENTRY = 100
        self.players = []
        self.name_font = pygame.font.SysFont("comicsans", 20, bold=True)
        self.score_font = pygame.font.SysFont("comicsans", 20)
        self.rank_font = pygame.font.SysFont("comicsans", 60)
        self.BORDER_THICKNESS = 5

    def draw(self, win):
        """
        Draws all elements inside leaderboar in rows of different color for 
        clarity. Each row will display a player and his/her score.
        :returns: None
        """
        scores = [(player.name, player.score) for player in self.players]
        scores.sort(key=lambda x: x[1], reverse=True)

        for i, score in enumerate(scores):
            if i % 2 == 0:
                color = (255,255,255)
            else:
                color = (200,200,200)

            # Draw text here
            pygame.draw.rect(win, color, (self.x, self.y + i*self.HEIGHT_ENTRY, self.WIDTH, self.HEIGHT_ENTRY))
            rank = self.rank_font.render("#" + str(i+1), 1, (0,0,0))
            win.blit(rank, (self.x + 10, self.y + i*self.HEIGHT_ENTRY + self.HEIGHT_ENTRY/2 - rank.get_height()/2))

            name = self.name_font.render(score[0], 1, (0,0,0))
            win.blit(name, (self.x - name.get_width()/2 + self.WIDTH/2, self.y + i*self.HEIGHT_ENTRY + 20))

            score = self.score_font.render("Score" + str(score[1]), 1, (0,0,0))
            win.blit(score, (self.x - name.get_width()/2 + self.WIDTH/2, self.y + i*self.HEIGHT_ENTRY + 40))

        pygame.draw.rect(win, (0,0,0),(self.x, self.y, self.WIDTH, self.HEIGHT_ENTRY*len(scores)), self.BORDER_THICKNESS)

    def add_player(self, player):
        """
        Append a player to players list.
        :player: Player
        :returns: None
        """
        self.players.append(player)

    def remove_player(self, player):
        """
        Removes a player from players list.
        :player: Player
        :returns: None
        """
        self.players.remove(player)
