import pygame
import Option
import TecladoControler

from Jugador import Personaje
from Construc import Muro

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
    


def INIT_Componente ():
    global player,Ventana,reloj,colision,Estructura,Estructura_2,Estructura_3

    #* Posicion Inicial
    X = Option.PosicionX
    Y= Option.PosicionY
    
    #* Referencia a personaje dentro de player
    player =  Personaje(X,Y)#? Ademas inicializa el personaje en la posicion inicial
     #? creamos una ventana con las escalas de anchura y altura
    Ventana =pygame.display.set_mode((Option.Ancho , Option.Altura))#variable para abreviar el codigo
    
    pygame.display.set_caption(Option.Ventana_name)#?Se establece el nombre de la ventana
    
    reloj = pygame.time.Clock()#?Se establece el reloj para abreviar el codigo
    
    colision = player.forma.colliderect #?establecer colision para abreviar codigo
    Estructura = Muro(200,200)
    Estructura_2 =Muro(400,400)
    Estructura_3 =Muro(600,200)
    
    
def game():
    #* Inicializar componentes
    INIT_Componente()
    
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
        PX,PY = TecladoControler.Update_Movement(PX,PY,Option,Velocidad,player)

        
        #?Colisiones
        
        if colision(Estructura.forma ) or colision(Estructura_2.forma ) or colision(Estructura_3.forma ) :
            #*Colision detectada
            
            player.Movimiento(-PX,-PY) #? Si hay colision se mueve en la direccion contraria


        DibujadoEnPantalla(Ventana) #! Esta funcion solo ordena el orden en que se renderiza ciertos objetos


        for event in pygame.event.get():#?bucle para reconocer que teclas se han presionado

            #*Evento salir
            Run =TecladoControler.Identifier_Exit(Run,event)
            
            #*Eventos de movimientos al tocar una tecla
            TecladoControler.Identifier_Key(event,Option)

        pygame.display.update(); #?Actualizar la pantalla
        


#*Ejecucion principal

pygame.init()

#* Juego principal
game()

pygame.quit()