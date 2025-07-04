
#? Global
import pygame
import os


#?Movimiento del Pacman
M_Izquierda = False
M_Derecha = False
M_Arriba = False
M_Atras = False


#?Ventana Variables
Ventana_name= "Pacman"
ColorFondo = (0,64,128) #* azul marino
fps = 120 #? Frames por segundo

pygame.init()
info = pygame.display.Info()


Ancho = info.current_w #1360
Altura = info.current_h -30#768

Fullscreen = False


#? pacman
ColorPersonaje = (225,225,128)#* amarillo
Velocidad = 5 #? Velocidad del pacman

    #* Posicion del pacman
PosicionX = 300
PosicionY = 300

Ancho_jugador = 39 #? Ancho del pacman
Altura_jugador = 39 #? Alto del pacman
