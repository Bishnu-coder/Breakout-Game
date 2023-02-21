import pygame
_=False
map1=[
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1]
]
#map class
class map():
    def __init__(self):
        self.main_lst=[]
        self.Rect_list=[]
        for j,row in enumerate(map1):
            for i ,column in enumerate(row):
                if column:
                    self.main_lst.append([i,j])
        for dinate in self.main_lst:
            self.Rect_list.append(pygame.Rect(dinate[0]*50,dinate[1]*50,47,47))
    def draw(self,Game,color):
        [pygame.draw.rect(Game.scren,color,rect) for rect in self.Rect_list]
        
if __name__ == "__main__":
    print(len(map1))
