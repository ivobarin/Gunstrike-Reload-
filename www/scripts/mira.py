import pygame
  
class Chosshair():
    def __init__(self) -> None:
        self.image = pygame.transform.scale(pygame.image.load('www/img/HUD/crosshair.png').convert_alpha(),(25,25))
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("www/sounds/gun-1.ogg")
        self.gunreload = pygame.mixer.Sound("www/sounds/reload.ogg")
        self.animation = ['www/img/HUD/0.png','www/img/HUD/1.png',
                          'www/img/HUD/2.png','www/img/HUD/3.png',
                          'www/img/HUD/4.png','www/img/HUD/5.png',
                          'www/img/HUD/6.png']
        self.bullets = 7
        self.frame = 0
        self.weapon =  pygame.image.load('www/img/HUD/gun.png').convert_alpha()
        self.box_item = pygame.transform.scale(pygame.image.load('www/img/HUD/box.png').convert(),(88,88))
    
    def shoot(self):
        self.bullets -= 1
        if(self.bullets > 0): 
            self.gunshot.set_volume(0.1)
            self.gunshot.play()
            self.frame += 1
        else:
            self.gunshot = pygame.mixer.Sound("www/sounds/no-ammo.ogg")
            self.gunshot.play()
            

    def reload(self):
        self.gunreload.set_volume(0.1)
        self.gunreload.play()
        self.bullets = 7
        self.frame = 0
        self.gunshot = pygame.mixer.Sound("www/sounds/gun-1.ogg")
    
    def update(self,window) -> None:
        self.rect.center = pygame.mouse.get_pos()
        self.image_bullets = pygame.image.load(self.animation[self.frame]).convert_alpha()
        window.blit(self.box_item,(-5,620))
        window.blit(self.image_bullets,(12,637))    
        window.blit(self.weapon,(85,645))    
        window.blit(self.image,self.rect)
    
    @property
    def get_bullets(self):
        return self.bullets

    @property
    def rectangle(self):
        return self.rect 
    
    def view_collision(self,screen,rect):
        pygame.draw.rect(screen,'blue',rect)
