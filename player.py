import pygame
#player class
class Payer():
    def __init__(self,Game):
        self.pos=Game.game_rect.midbottom
        self.rect_ply=pygame.Rect(self.pos[0]-20,self.pos[1]-20,150,20)
        self.speed=5
    def draw(self,Game):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect_ply.x-=self.speed
        if keys[pygame.K_RIGHT]:
            self.rect_ply.x+=self.speed
        if self.rect_ply.x <= 0:
            self.rect_ply.x=0
        if self.rect_ply.x >= 450:
            self.rect_ply.x=450
        pygame.draw.rect(Game.scren,'green',self.rect_ply)