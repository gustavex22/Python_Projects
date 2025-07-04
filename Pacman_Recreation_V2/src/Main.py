import pygame
import os
from numpy.ma.mrecords import fromrecords

from Pacman_Recreation_V2.src.settings import Options
from Pacman_Recreation_V2.src.Entities.Player import pacman
from Pacman_Recreation_V2.src.Input import Teclado_Controller
from Pacman_Recreation_V2.src.Input import Ventana_Controller

#TODO Recreacion del juego pacman

""" 
    Explicacion:
Reacreare el juego de pacman ,sin usar spriter solo por medio del codigo en python
NO esta permitido usar spriter originales todo se dibujara mediante codigo 
NO esta permitido ver el codigo original del juego explicitamente o otra recreacion
Solo se permite ver tuto,documentales y lo necesario para aprender y recrear el codigo de pacman en python

"""
"""
#?Actividades
-Movimiento
    -Diseñode personaje Basicas (Movimientos , colisiones con objetos):semiTerminado
    -Implementar Condicion para colisiones solo con los objetos cercanos 
    
-Diseño mapas y Coordenadas
    -Cargador de mapas

-Diseño personajes
    -pacman        
    -Fantasmas
    
-Algoritmo de busqueda y persecucion de los fantasmas

"""

def Init_Components(): #! Inicializa los componentes del juego
    global Ventana,reloj,settings,velocidad,jugador

    #* Referencias
    settings = Options

    ancho = settings.Ancho
    altura = settings.Altura

    velocidad = settings.Velocidad
    PX = settings.PosicionX
    PY = settings.PosicionY

    os.environ['SDL_VIDEO_WINDOW_POS'] = "0,30"
    #* Inicializa pygame
    pygame.init()

    Ventana = pygame.display.set_mode((ancho, altura),pygame.RESIZABLE)#* Se crea una ventana con las escalas de ancho y alto

    pygame.display.set_caption(settings.Ventana_name)#* Se establece el nombre de la ventana

    reloj = pygame.time.Clock()#* Se usa la funcion Clock para establecer los fps

    #* Player
    jugador = pacman(PX, PY, settings) #* Se crea el jugador en la posicion inicial


def Ventana_draw(Interfaz,Options):
    jugador.draw(Interfaz,Options)


#todo Inicializar juego

def Main():

    Run = True
    Init_Components()
    global Ventana

    # Bucle del juego
    while Run:
        # ? Inicializar variables
        Y = 0
        X = 0

        reloj.tick(settings.fps)  # FPS de la ventana
        Ventana.fill(settings.ColorFondo)  # Fondo de la ventana

        X, Y = Teclado_Controller.Update_Movement(X, Y, settings, velocidad, jugador)

        Ventana_draw(Ventana, settings)  # ! Dibuja el jugador en la ventana

        # todo Identificador de teclas
        for event in pygame.event.get():  # ?bucle para reconocer que teclas se han presionado

            # * Actualiza la ventana opciones
            Ventana = Ventana_Controller.UpdateInfo(event,settings,Ventana) #fullscreen(event,settings,Ventana)

            # *Evento salir
            Run = Teclado_Controller.Tecla_Exit(Run, event)

            # *Eventos de movimientos al tocar una tecla
            Teclado_Controller.Tecla_Identity(event, settings,Ventana)

        pygame.display.update()  # ! Actualiza la pantalla


if __name__ == "__main__":
    Main()