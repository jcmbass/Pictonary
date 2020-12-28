import pygame
from button import Button, TextButton
from board import Board
from top_bar import TopBar
from main_menu import MainMenu
from menu import Menu
from tool_bar import ToolBar
from leaderboard import Leaderboard
from player import Player
from bottom_bar import BottomBar
from chat import Chat

class Game(object):

    """Handles all logic for game in client side, it stores every object that player is able to
    interact and manipulate. Methods are responsible for listening when a player
    is interacting with his mouse.
    """
    BG = (255,255,255)
    def __init__(self):
        """Instantiate the game object and its properties. """
        self.WIDTH = 1300
        self.HEIGHT = 1000
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.leaderboard = Leaderboard(50, 125)
        self.board = Board(305, 125)
        self.top_bar = TopBar(10, 10, 1280, 100)
        self.players = []
        self.skip_button = TextButton(85, 825, 125, 60, (255,255,0), "skip")
        self.bottom_bar = BottomBar(305, 880, self)
        self.chat = Chat(1050, 125)
        self.draw_color = (0,0,0)
        for player in self.players:
            self.leaderboard.add_player(player)

    def draw(self):
        """
        Draws all elements in window.
        :returns: None
        """
        self.win.fill(self.BG)
        self.leaderboard.draw(self.win)
        self.top_bar.draw(self.win)
        self.board.draw(self.win)
        self.skip_button.draw(self.win)
        self.bottom_bar.draw(self.win)
        self.chat.draw(self.win)
        pygame.display.update()

    def check_clicks(self):
        """
        handles clicks on buttons and screen
        :returns: None
        """
        mouse = pygame.mouse.get_pos()
        if self.skip_button.click(*mouse):
            print("mouse cliked")

        clicked_board = self.board.click(*mouse)
        if clicked_board:
            self.board.update(*clicked_board, self.draw_color)

    def run(self):
        """
        Runs on background and listen to all events.
        If mouse is pressed calls the right actions.
        :returns: None

        """
        run = True
        #clock = pygame.time.Clock()
        while run:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if pygame.mouse.get_pressed()[0]:
                    self.check_clicks()
                    self.bottom_bar.button_events()
        pygame.quit()

if __name__ == "__main__":
    pygame.font.init()
    g = Game()
    g.run()
