"""
Represents the leaderboard object for the client side of the game.
"""
import pygame

class Leaderboard(object):
    """
    docstring
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIDTH = 200
        self.HEIGHT_ENTRY = 100
        self.players = []
        self.name_font = pygame.font.SysFont("comicSans", 30, bold=True)
        self.score_font = pygame.font.SysFont("comicSans", 20)
        self.rank_font = pygame.font.SysFont("comicSans", 50, bold=True)

    def draw(self, win):
        """
        docstring
        """
        scores = [(player.name, player.score) for player in self.players]
        scores.sort(key=lambda x: x[1], reverse=True)

        for i, score in enumerate(scores):
            if i % 2 == 0:
                color = (255,255,255)
            else:
                color = (120, 120, 120)
            
            # Draw text here
            pygame.draw.rect(win, (self.x, self.y + i*self.HEIGHT_ENTRY, self.WIDTH, self.HEIGHT_ENTRY))
            rank = self.rank_font.render("#" + str(i+1), 1, (0,0,0))
            win.blit(rank, (self.x + 10, self.y + i*self.HEIGHT_ENTRY + 10))

            name = self.name_font.render(score[0], 1, (0,0,0))
            win.blit(name, (self.x - name.get_width()/2 + self.WIDTH/2, self.y + i*self.HEIGHT_ENTRY + 20))

            score = self.score_font.render(score[1], 1, (0,0,0))
            win.blit(score, (self.x - name.get_width()/2 + self.WIDTH/2, self.y + i*self.HEIGHT_ENTRY + 40))

    def add_player(self, player):
        """
        docstring
        """
        self.players.append(player)

    def remove_player(self, player):
        """
        docstring
        """
        self.players.remove(player)