##########################################################################
#                                                                        #
# [To remember]:"small case name for class"                              #
# [To remember]:"upper case starting name for class containing variable" #
#                                                                        #
##########################################################################

# IMPORTS

import pygame
from maps import map
from player import Payer
from rich import print
from pygamergui import tools, window

# GAME CLASS


class game:
    """the actual game class that handel the game"""
    def __init__(self):
        pygame.init()
        self.w = 600
        self.h = 600
        self.scren = pygame.display.set_mode((self.w,self.h))
        self.game_rect = self.scren.get_rect()
        pygame.display.set_caption("block_game")
        self.clock = pygame.time.Clock()

    def update(self):
        """code for updating the game"""
        while True:
            self.scren.fill('black')
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if Ball.y >= 590:
                    print("[red]Game over[/red]")
                    pygame.quit()
                    quit(0)
            Ball.update()
            Map.draw(self,'red')
            Player.draw(Game)
            pygame.display.update()
            self.clock.tick(60)
# BALL CLASS


class ball:
    def __init__(self):
        self.r = 10
        self.xs = 3
        self.ys = 3
        self.x = Player.pos[0]
        self.y = Player.pos[1]-Player.rect_ply.height
        self.circle = pygame.draw.circle(Game.scren,'white',(self.x,self.y),self.r)

    def check(self):
        if self.x >= 600 or self.x <= 0:
            self.xs *= -1
        if self.circle.colliderect(Player.rect_ply):
            self.ys *= -1
        if self.x <= 0:
            self.ys *= -1
        if self.y <= 0:
            self.ys *= -1
        if self.y >= 600:
            print("[red] Game over [/red]")
            quit(0)
        for rect in Map.Rect_list:
            if self.circle.colliderect(rect):
                self.ys *= -1
                Map.Rect_list.remove(rect)
        self.x -= self.xs
        self.y -= self.ys

    def update(self):
        """function for updating state of ball"""
        self.check()
        self.circle=pygame.draw.circle(Game.scren,'white',(self.x,self.y),self.r)
# STUFF FOR BEGINNING OF GAME

def update():
    text = tools.text("BREAK OUT", color='cyan')
    text2 = tools.text("By pygamer", size=24, color='red')
    start_button = tools.simple_button(text="play", fg='green', w=85, h=85, color='lightblue', target=start)
    text.show(display, 200, 100)
    text2.show(display, 250, 150)
    start_button.show_color_change(260, 300, display, corner_round_level=3)

# ACTUAL GAME STARTING CODE


def start(co):
    global Game , Map, Player, Ball # ----making these variables global is important
    Game = game()  # ----------loading the game class
    Map = map()  # ------------loading the map from map.py file
    Player = Payer(Game)  # ---loading the player
    Ball = ball()  # ----------loading the ball
    Game.update()  # ----------updating the whole game

# TESTING


display = window.app(target=update)
display.run()

