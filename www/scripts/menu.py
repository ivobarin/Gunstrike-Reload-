import pygame 
import sys
import sqlite3

class Menus:
    def __init__(self):
        self.state = 'Menu'
        self.img_menu = pygame.image.load(r"www\img\title.png")
        self.img_ranking = pygame.image.load(r"www\img\ranking.png")
        self.img_submit = pygame.image.load(r"www\img\submit.png")
        self.img_game_over = pygame.image.load(r"www\img\Game_Over.png")
        self.music = pygame.mixer.Sound('www\sounds\el_macho.ogg')
        self.scores = []
        self.score_final = 0 
        self.texto_score = 0
        self.flag_submit = False 
        self.flag_scores = False 
        self.font = pygame.font.Font(r"www\font\Westhorn-Regular.ttf", 40)
        self.input = ""
        self.input_rect = pygame.Rect(324,296,473,55)

    
    def mostrar_menu(self,screen):
        pygame.mouse.set_visible(True)
        lista_eventos = pygame.event.get()
        
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONUP:
                lista_click = list(evento.pos)
                
                if lista_click[0] > 501 and lista_click[0] < 705 and lista_click[1] > 261 and lista_click[1] < 317.32:
                    self.state = 'Start Game'
                elif lista_click[0] > 501 and lista_click[0] < 705 and lista_click[1] > 344 and lista_click[1] < 400.32:
                    self.state = 'Ranking'
                elif lista_click[0] > 501 and lista_click[0] < 705 and lista_click[1] > 427 and lista_click[1] < 483.32:
                    pygame.quit()
                    sys.exit()
                
        self.music.set_volume(0.1)
        self.music.play(-1)
        screen.blit(self.img_menu,(0,0))
        pygame.display.flip()

    def mostrar_ranking(self,screen):
        pygame.mouse.set_visible(True)
        
        if not self.flag_scores:
            with sqlite3.connect("bd_btf.db") as conexion:
                try:
                    sentencia = "SELECT * FROM usuarios ORDER BY score DESC"
                    self.scores = conexion.execute(sentencia).fetchall()
                    self.flag_scores = False  
                except Exception:
                    print(f"Error")
        
        primero = list(self.scores[0])
        segundo = list(self.scores[1])
        tercero = list(self.scores[2])  
        cuarto = list(self.scores[3])
        quinto = list(self.scores[4])

        lista_eventos = pygame.event.get()
        
        # para agregar imput
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONUP:
                lista_click = list(evento.pos)
                if lista_click[0] > 44 and lista_click[0] < 182 and lista_click[1] > 22 and lista_click[1] < 78:
                    self.flag_submit = False
                    self.state = 'Menu'
                    
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    self.input = self.input[0:-1]  # Método slice
                elif evento.key == pygame.K_RETURN:
                    with sqlite3.connect("bd_btf.db") as conexion:
                        try:
                            conexion.execute("insert into usuarios(nombre,score) values (?,?)", (self.input,self.score_final))
                        except Exception as exepcion:
                            print(f"Error: {exepcion}")
                    
                    print("Texto ingresado:", self.input)
                    self.input = ""
                    self.flag_submit = False
                    self.flag_scores = False 
                    self.state = 'Menu'
                else:
                    self.input += evento.unicode  #
                            
        
        render_nombre_1 = self.font.render(f"{primero[1]}",True,'azure')
        render_nombre_2 = self.font.render(f"{segundo[1]}",True,'azure')
        render_nombre_3 = self.font.render(f"{tercero[1]}",True,'azure')
        render_nombre_4 = self.font.render(f"{cuarto[1]}",True,'azure')
        render_nombre_5 = self.font.render(f"{quinto[1]}",True,'azure')
        render_score_1 = self.font.render(f"{primero[2]}",True,'azure')
        render_score_2 = self.font.render(f"{segundo[2]}",True,'azure')
        render_score_3 = self.font.render(f"{tercero[2]}",True,'azure')
        render_score_4 = self.font.render(f"{cuarto[2]}",True,'azure')
        render_score_5 = self.font.render(f"{quinto[2]}",True,'azure')
        
        screen.blit(self.img_ranking,(0,0))
        screen.blit(render_nombre_1,(316,287))
        screen.blit(render_nombre_2,(316,367))
        screen.blit(render_nombre_3,(316,467))
        screen.blit(render_nombre_4,(316,550))
        screen.blit(render_nombre_5,(316,630))
        
        screen.blit(render_score_1,(765,287))
        screen.blit(render_score_2,(765,367))
        screen.blit(render_score_3,(765,467))
        screen.blit(render_score_4,(765,550))
        screen.blit(render_score_5,(765,630))
                            
        # input
        if self.flag_submit == True:
            screen.blit(self.img_submit,(0,0))
            pygame.draw.rect(screen, 'white', self.input_rect,0,25)
            texto_input = self.font.render(self.input, True, 'black')
            screen.blit(texto_input, (self.input_rect.x + 25, self.input_rect.y + 5))
        pygame.display.flip()

    def mostrar_game_over(self,screen): 
        pygame.mouse.set_visible(True)
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONUP:
                lista_click = list(evento.pos)
                
                if lista_click[0] > 390 and lista_click[0] < 581 and lista_click[1] > 380 and lista_click[1] < 451:
                    self.state = 'Menu'
                elif lista_click[0] > 616 and lista_click[0] < 807 and lista_click[1] > 380 and lista_click[1] < 451:
                    self.flag_submit = True 
                    self.state = 'Ranking'
        
            screen.blit(self.img_game_over,(0,0))
            screen.blit(self.texto_score,(660,295))
        pygame.display.flip()
        
    def estado_menu(self,screen):
        retorno = False 
        if self.state == 'Menu':
            self.mostrar_menu(screen)
        elif self.state == 'Start Game':
            self.music.stop()
            retorno = True
        elif self.state == 'Ranking':
            self.mostrar_ranking(screen)
        elif self.state == 'Game Over':
            retorno = False       
            self.mostrar_game_over(screen)
        return retorno
    
    def volver_menu(self):
        self.state = 'Menu'
    
    def endgame(self,texto_score,score_num):
        self.state = 'Game Over'
        self.texto_score = texto_score
        self.score_final = score_num
        