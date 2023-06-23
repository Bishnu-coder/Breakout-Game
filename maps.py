import pygame #--importing pygame
_=False #---setting _ to False
map1=[
    [2,1,1,1,1,1,1,1,1,1,1,1],
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
        [pygame.draw.rect(Game.scren,color,rect,border_radius=3) for rect in self.Rect_list]
        
# if __name__ == "__main__":
#     Map=map()
#     print(map1[0][0])
