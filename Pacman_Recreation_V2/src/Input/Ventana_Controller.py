import pygame
global screen

def fullscreen(event, Option, ventana):

    if event.type == pygame.KEYDOWN and event.key == pygame.K_F11 :
        if not Option.Fullscreen:
            ventana = pygame.display.set_mode((Option.Ancho,Option.Altura), pygame.FULLSCREEN)
            Option.Fullscreen = True

        else:
            # Solo el flag RESIZABLE, sin FULLSCREEN
            ventana = pygame.display.set_mode((Option.Ancho, Option.Altura), pygame.RESIZABLE)
            Option.Fullscreen = False

    return ventana


def UpdateInfo(event, Option, ventana):

        if event.type == pygame.VIDEORESIZE and not Option.Fullscreen:
            Option.Ancho = event.w
            Option.Altura = event.h

            ventana = pygame.display.set_mode((Option.Ancho, Option.Altura), pygame.RESIZABLE)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11 :
            if not Option.Fullscreen:
                Option.Altura += 30
                ventana = pygame.display.set_mode((Option.Ancho,Option.Altura), pygame.FULLSCREEN)
                Option.Fullscreen = True

            else:
                # Solo el flag RESIZABLE, sin FULLSCREEN
                Option.Altura -= 30
                ventana = pygame.display.set_mode((Option.Ancho, Option.Altura), pygame.RESIZABLE)
                Option.Fullscreen = False

        return ventana
