import pygame
import Option
from Jugador import Personaje
from Estructuras import Muro

""" 
Recreacion del juego pacman

#?Explicacion
Reacreare el juego de pacman ,sin usar spriter solo por medio del codigo en python
NO esta permitido usar spriter originales todo se dibujara mediante codigo 
NO esta permitido ver el codigo original del juego explicitamente o otra recreacion
Solo se permite ver tuto,documentales y lo necesario para aprender y recrear el codigo de pacman en python

#?Actividades
-Movimiento(listo)
-Colisiones(listo)
-Mapas
-Fantasmas
-IA de los fantasmas
-Algoritmo de busqueda y persecuacion para los Fantasmas
"""

def DibujadoEnPantalla(Ventana):
    player.draw(Ventana)#*Dibuja al jugador
    Estructura.drawEstructure(Ventana,(0,0,128))#*Dibuja el muro
    Estructura_2.drawEstructure(Ventana,(0,0,128))
    Estructura_3.drawEstructure(Ventana,(0,0,128))
    


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
        #player.draw(Ventana)
        
        #?Movimiento posicion y veloidad
        PX = 0
        PY = 0
        Velocidad = Option.Velocity
        
        #? Sentencias If de movimiento
        
        if Option.M_Izquierda == True:
            PX -=  Velocidad
        if Option.M_Derecha == True:
            PX += Velocidad
        if Option.M_Arriba == True:
            PY -= Velocidad
        if Option.M_Atras == True:
            PY  += Velocidad
        
        player.Movimiento(PX,PY) #?Actualiza el movimiento del jugador

       
        colision = player.forma.colliderect
        #?Colisiones
        if colision(Estructura.forma ) or colision(Estructura_2.forma ) or colision(Estructura_3.forma ) :
            
            #*Colision detectada
            print("Colision Detectada")
            player.Movimiento(-PX,-PY) #? Si hay colision se mueve en la direccion contraria
           
        else:
            print("Colision No Detectada")
            
        DibujadoEnPantalla(Ventana) #! Esta funcion solo ordena el orden en que se renderiza ciertos objetos

        
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
                #! Al dejar de tocar una tecla ,(Por si acaso, no es necesario esta parte del codigo )
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

Estructura = Muro(200,200)
Estructura_2 =Muro(400,400)
Estructura_3 =Muro(600,200)

#* Juego principal
game()

pygame.quit()