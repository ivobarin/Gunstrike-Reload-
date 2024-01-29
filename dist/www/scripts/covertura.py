import pygame
class Cover(pygame.sprite.Sprite):
    def __init__(self,path,pos_x,pos_y,scale_x,scale_y) -> None:
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(),(scale_x,scale_y))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        self.clicked = False
    
    @property
    def rectangle(self):
        return self.rect 
    
    def view_collision(self,screen,rect):
        pygame.draw.rect(screen,'green',rect)
