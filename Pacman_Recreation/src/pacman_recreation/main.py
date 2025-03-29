import pygame
import Option
from Jugador import Personaje

""" 
Recreacion del juego pacman
#?Explicacion
Reacreare el juego de pacman ,sin usar spriter solo pro medio del codigo en python
NO esta permitido usar spriter originales todo se dibujara mediante codigo 
NO esta permitido ver el codigo original del juego explicitamente o otra recreacion
Solo se permite ver tuto,documentales y lo necesario para aprender y recrear el codigo de pacman en python

#?Actividades
-Movimiento(listo)
-Colisiones
-Fantasmas
-IA de los fantasmas
-Algoritmo de busqueda y persecuacion para los Fantasmas
"""

def game():
    #? creamos una ventana con las escalas de anchura y altura
    Ventana =pygame.display.set_mode((Option.Ancho , Option.Altura))#variable para abreviar el codigo
    
    pygame.display.set_caption(Option.Ventana_name)#?Se establece el nombre de la ventana
    
    reloj = pygame.time.Clock()#?Se establece el reloj para abreviar el codigo
    
    Run=True
    
    while(Run):
        #*Codigo del juego aqui
        
        #?S usara el modulo reloj para establecer los fps
        reloj.tick(Option.fps)
        
        #?establecer color de fondo
        Ventana.fill(Option.ColorFondo)
        
        #?Dibujar jugador
        player.draw(Ventana)
        
        #?Movimiento posicion
        PX = 0
        PY = 0
        Velocidad = 5
        
        #? Sentencias If de movimiento
        
        if Option.M_Izquierda == True:
            PX -=  Velocidad
        if Option.M_Derecha == True:
            PX += Velocidad
        if Option.M_Arriba == True:
            PY -= Velocidad
        if Option.M_Atras == True:
            PY  += Velocidad
        
        player.Movimiento(PX,PY)
        player.draw(Ventana)
        
        #?bucle para reconocer que teclas se han presionado
        for event in pygame.event.get():
            
            #*Evento salir
            if event.type == pygame.QUIT:
                Run = False
                
            #*Eventos de movimientos al tocar una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    Option.M_Izquierda = True
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    Option.M_Derecha = True
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    Option.M_Atras = True
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    Option.M_Arriba = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    Option.M_Izquierda = False
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    Option.M_Derecha = False
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    Option.M_Arriba = False
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    Option.M_Atras = False
        
        pygame.display.update(); #?Actualizar la pantalla
        


#*Ejecucion principal

pygame.init()

#* Posicion Inicial
X = Option.PosicionX
Y= Option.PosicionY

#* Referencia a personaje dentro de player
player =  Personaje(X,Y)#? Ademas inicializa el personaje en la posicion inicial

#* Juego principal
game()

pygame.quit()