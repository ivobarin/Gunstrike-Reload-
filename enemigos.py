import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,path,pos_x,pos_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(),(75,75))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x  # Posición inicial en el eje X
        self.rect.y = pos_y  # Posición inicial en el eje Y
        self.origin_pos = pos_y
        self.subiendo = True 
        self.quito = False
        self.tiempo = 0
    
    @property
    def rectangle(self):
        return self.rect 
    
    def mover_eje_y(self, time_ms, top, buttom, freeze, speed_up, speed_down):
        if not self.quito:
            if self.subiendo:
                self.rect.y -= speed_up
            else:
                self.rect.y += speed_down

        if (self.subiendo and self.rect.y <= top) or (not self.subiendo and self.rect.y >= buttom):
            self.tiempo += time_ms
            self.quito = True

            if self.tiempo > freeze:
                self.subiendo = not self.subiendo #invertimos el valor
                self.quito = False
                self.tiempo = 0

        
    def mover_eje_x(self, time_ms, left, right, freeze, speed_up, speed_down):
        if not self.quito:
            if self.subiendo:
                self.rect.x -= speed_up
            else:
                self.rect.x += speed_down
    
        if (self.subiendo and self.rect.x <= left) or (not self.subiendo and self.rect.x >= right):
            self.tiempo += time_ms
            self.quito = True
    
            if self.tiempo > freeze:
                self.subiendo = not self.subiendo #invertimos el valor
                self.quito = False
                self.tiempo = 0

                    
    def view_collision(self,screen,rect):
        pygame.draw.rect(screen,'red',rect)