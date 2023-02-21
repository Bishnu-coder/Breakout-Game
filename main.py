#imports
import pygame
from maps import map
from player import Payer
#map class
Map=map()
#game class
class game():
    def __init__(self):
        pygame.init()
        self.w=600
        self.h=600     
        self.scren = pygame.display.set_mode((self.w,self.h))
        self.game_rect=self.scren.get_rect()
        pygame.display.set_caption("block_game")
        self.clock=pygame.time.Clock()
    def update(self):
        while True:
            self.scren.fill('black')
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    exit()
                if Ball.y>=600:
                    print("Game over")
                    exit(0)
            Ball.update()
            Map.draw(self,'red')
            Player.draw(Game)
            pygame.display.update()
            self.clock.tick(60)
Game=game()
#ball_class
class ball():
    def __init__(self):
        self.r=10
        self.xs=3
        self.ys=3
        self.x=Player.pos[0]
        self.y=Player.pos[1]-Player.rect_ply.height
        self.circle=pygame.draw.circle(Game.scren,'white',(self.x,self.y),self.r)
    def check(self):
        if self.x>=600 or self.x<=0:
            self.xs*=-1
        if self.circle.colliderect(Player.rect_ply):
            self.ys*=-1
        if self.x<=0:
            self.ys*=-1
        for rect in Map.Rect_list:
            if self.circle.colliderect(rect):
                self.ys*=-1
                Map.Rect_list.remove(rect)
        self.x-=self.xs
        self.y-=self.ys
    def update(self):
        self.check()
        self.circle=pygame.draw.circle(Game.scren,'white',(self.x,self.y),self.r)
#player class
Player=Payer(Game)
Ball=ball()
Game.update()
