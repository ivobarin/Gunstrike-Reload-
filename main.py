import pygame, sys
from mira import Chosshair
from covertura import Cover
from enemigos import Enemy
from constantes import *
from menu import Menus

# - Configuracion de pantalla        
pygame.init()
pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Gunstrike Reload")

# - Icono
pygame.display.set_icon(pygame.transform.scale(pygame.image.load("img/icono.jpg").convert(),(16,16)))

# - Imagenes 
img_cielo = pygame.transform.scale(pygame.image.load('img/sky.png').convert(),(1200,250))
img_piso = pygame.image.load('img/piso.png').convert()

# - Render
font = pygame.font.SysFont("pixellari",40,False,True)

# - Score 
img_score = pygame.transform.scale(pygame.image.load('img/Score.png'),(200,100))
img_score.set_colorkey((30,30,30))
score_total = 0 
texto_score = font.render(str(score_total),True,COLOR_ASSETS)
score_final = 0 

# - Timer 
tiempo = TIEMPO
evento_tiempo = pygame.USEREVENT + 1
pygame.time.set_timer(evento_tiempo,500)
img_timer = pygame.transform.scale(pygame.image.load('img/Timer.png'),(200,100))
img_timer.set_colorkey((30,30,30))

# - Bandera debug
flag_debug = False

# - Tiempo 
clock = pygame.time.Clock()

# - Creamos la mira 
crosshair = Chosshair()

# - Creamos las coverturas 
covertura_1 = Cover('img/items/barrel.png',100,500,85,85)
covertura_2 = Cover('img/items/barrel.png',300,500,85,85)
covertura_3 = Cover('img/items/cactus-1.png',375,230,75,130)
covertura_4 = Cover('img/items/cactus-1.png',800,230,75,130)
covertura_5 = Cover(r'img\items\rock-4.png',1060,300,75,100)
covertura_6 = Cover(r'img\items\rock-5.png',1010,340,65,35)
covertura_7 = Cover('img/items/barrel.png',600,500,85,85)
covertura_8 = Cover('img/items/barrel.png',850,500,85,85)
covers = pygame.sprite.Group()
covers.add(covertura_1,covertura_2,covertura_3,covertura_4,covertura_5,covertura_6,covertura_7,covertura_8)

# - Grupo de enemigos 
enemies = pygame.sprite.Group()

# - Bandera de enemigos lvl 1
flag_new_enemies_lv1 = True 
flag_move_enemies_lv1 = True 

# - Bandera de enemigos lvl 2
flag_new_enemies_lv2 = False 
flag_move_enemies_lv2 = False 

# - Creamos el menu
menu_principal = Menus()

# loop del juego
while True:
    # si el estado del objeto es  
    if menu_principal.estado_menu(pantalla):        
        # no se muestra el mouse pero podemos usar las coordenadas 
        pygame.mouse.set_visible(False)
        
        # lista de eventos
        lista_eventos = pygame.event.get()
        lista_mouse = pygame.mouse.get_pressed()
        lista_teclado = pygame.key.get_pressed()
        
        # bucle de eventos  
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # click derecho
                if lista_mouse[0]:
                    crosshair.shoot()
                    # si tiene balas 
                    if(crosshair.get_bullets > 0):
                        # si la colicion del mouse no esta con una covertura
                        if not pygame.sprite.spritecollide(crosshair,covers,False):
                        # coliciona el click del mouse (rect) con los enemigos 
                            if pygame.sprite.spritecollide(crosshair,enemies,True):
                                score_total += 10
                                texto_score = font.render(str(score_total),True,COLOR_ASSETS)
                # click izquierdo 
                elif lista_mouse[2]:
                    crosshair.reload()   
            # cronometro tiempo 
            elif evento.type == evento_tiempo:
                tiempo -= 1 
            # debug 
            if True in lista_teclado:
                if lista_teclado[pygame.K_z]:
                    flag_debug = True
                if lista_teclado[pygame.K_x]:
                    flag_debug = False 
                

        # fondos 
        pantalla.blit(img_piso,(0,0))
        pantalla.blit(img_cielo,(0,0))
            
        # - Creamos los enemigos y los agrupamos por niveles  
        # - nivel 1
        if flag_new_enemies_lv1:
            enemigo1 = Enemy('img/enemies/cowboy/ranger.png',63,445)
            enemigo2 = Enemy('img/enemies/cowboy/ranger.png',263,445)
            enemigo3 = Enemy('img/enemies/cowboy/ranger.png',340,210)
            enemigo4 = Enemy('img/enemies/cowboy/ranger.png',770,210)
            enemigo5 = Enemy('img/enemies/cowboy/ranger.png',565,445)
            enemigo6 = Enemy('img/enemies/cowboy/ranger.png',815,445)
            enemies.add(enemigo1,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6)
            flag_new_enemies_lv1 = False 
        
        # - nivel 2
        elif flag_new_enemies_lv2:
            enemigo1 = Enemy('img\enemies\cowboy\gunslinger.png',63,465)
            enemigo2 = Enemy('img\enemies\cowboy\gunslinger.png',263,465)
            enemigo3 = Enemy('img\enemies\cowboy\gunslinger.png',340,210)
            enemigo4 = Enemy('img\enemies\cowboy\gunslinger.png',770,210)
            enemigo5 = Enemy('img\enemies\cowboy\gunslinger.png',565,465)
            enemigo6 = Enemy('img\enemies\cowboy\gunslinger.png',815,465)
            enemigo7 = Enemy('img\enemies\cowboy\gunslinger.png',1015,275)
            enemies.add(enemigo1,enemigo2,enemigo3,enemigo4,enemigo5,enemigo6,enemigo7)
            flag_new_enemies_lv2 = False  
        
        # - milisegundos 
        ms = clock.tick(FPS)

        # - movimiento enemigos lvl_1
        if flag_move_enemies_lv1:
            enemigo1.mover_eje_y(ms,410,460,1500,4,5)
            enemigo2.mover_eje_y(ms,410,460,1000,3,5)
            enemigo3.mover_eje_x(ms,220,340,3000,3,4)
            enemigo4.mover_eje_x(ms,660,770,2000,2,4)
            enemigo5.mover_eje_y(ms,410,460,1000,4,4)
            enemigo6.mover_eje_y(ms,410,460,1500,3,5)

        # - movimiento enemigos lvl_2 
        elif flag_move_enemies_lv2: 
            enemigo1.mover_eje_y(ms,430,465,500,8,8)
            enemigo2.mover_eje_y(ms,430,465,700,5,6)
            enemigo3.mover_eje_x(ms,280,340,500,8,8)
            enemigo4.mover_eje_x(ms,700,770,700,8,8)
            enemigo5.mover_eje_y(ms,430,465,300,8,4)
            enemigo6.mover_eje_y(ms,430,465,800,4,5)
            enemigo7.mover_eje_x(ms,985,1015,750,7,4)
                
        # - si mueren los enemigos, vuelven aparecer 
        if len(enemies) == 0:
            if flag_move_enemies_lv1:
                flag_new_enemies_lv2 = True 
                flag_move_enemies_lv2 = True 
                flag_move_enemies_lv1 = False
            elif flag_move_enemies_lv2:
                flag_new_enemies_lv1 = True
                flag_move_enemies_lv1 = True
                flag_move_enemies_lv2 = False 

        # - mostrar enemigos
        enemies.draw(pantalla)

        # - coverturas 
        covers.draw(pantalla)

        # - Mira (jugador)
        crosshair.update(pantalla) # actualiza la posicion del Rect 

        # - Score
        pantalla.blit(img_score,(0,0))
        pantalla.blit(texto_score,(105,35))

        # - timer
        pantalla.blit(img_timer,(1000,0))
        texto = f'{tiempo:02d}'
        render = font.render(texto,True,COLOR_ASSETS)
        pantalla.blit(render,(1105,35))
        
        # debug colicciones
        if flag_debug:
            for enemy in enemies:
                enemy.view_collision(pantalla,enemy.rectangle)
            for cover in covers:
                cover.view_collision(pantalla,cover.rectangle)
            crosshair.view_collision(pantalla,crosshair.rectangle)
        
        # se termina el tiempo 
        if tiempo == 0:
            if len(enemies) > 0:
                enemies.empty()
           
            flag_new_enemies_lv1 = True 
            flag_move_enemies_lv1 = True 
            flag_new_enemies_lv2 = False 
            flag_move_enemies_lv2 = False 
            score_final = score_total
            texto_score_final = font.render(str(score_total),True,COLOR_ASSETS) 
            score_total = 0 
            texto_score = font.render(str(score_total),True,COLOR_ASSETS)
            tiempo = TIEMPO
            menu_principal.endgame(texto_score_final,score_final)
        
        pygame.display.flip()
        clock.tick(FPS)
