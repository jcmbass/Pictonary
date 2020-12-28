"""
Represents the chat for the game
"""
import pygame

class Chat(object):

    """Docstring for Chat. """

    def __init__(self, x, y):
        """TODO: to be defined.

        :x: TODO
        :y: TODO

        """
        self.x = x
        self.y = y
        self.WIDTH = 225
        self.HEIGHT = 800
        self.BORDER_THICKNESS = 5
        self.content = ["Hello" for _ in range(100)]
        self.typing = ""
        self.chat_font = pygame.font.SysFont("comicsans", 20)
        self.CHAT_GAP = 20

    def update_chat(self, msg):
        """TODO: Docstring for update_chat.

        :msg: TODO
        :returns: TODO

        """
        self.content.append(msg)

    def draw(self, win):
        """TODO: Docstring for draw.

        :win: TODO
        :returns: TODO

        """
        pygame.draw.rect(win, (200, 200, 200), (self.x, self.y + self.HEIGHT - 40, self.WIDTH, 40))
        pygame.draw.line(win, (0,0,0), (self.x, self.y + self.HEIGHT - 40), (self.x + self.WIDTH, self.y + self.HEIGHT - 40), self.BORDER_THICKNESS)
        pygame.draw.rect(win, (0,0,0), (self.x, self.y, self.WIDTH, self.HEIGHT), self.BORDER_THICKNESS)
        while len(self.content) * self.CHAT_GAP > self.HEIGHT - 60:
            self.content = self.content[:-1]

        for i, chat in enumerate(self.content):
            txt = self.chat_font.render(" - " + chat, 1,(0,0,0))
            win.blit(txt, (self.x + 8,10 + self.y + i*self.CHAT_GAP))

        type_chat = self.chat_font.render(self.typing, 1, (0,0,0))
        win.blit(type_chat, (self.x + 5, self.y + 50 - type_chat.get_height()/2))

    def type(self, char, delete=False):
        """TODO: Docstring for type.

        :char: TODO
        :returns: TODO

        """
        if delete:
            if len(self.typing) > 0:
                self.typing = self.typing[:-1]
        else:
            self.typing += char
