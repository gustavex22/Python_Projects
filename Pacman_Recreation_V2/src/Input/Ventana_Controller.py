import pygame

def fullscreen(event,Option,ventana):

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F11:
            if not fullscreen:
                ventana = pygame.display.set_mode((1360, 768), pygame.FULLSCREEN)
            else:
                ventana = pygame.display.set_mode((Option.Altura,Option.Ancho),pygame.RESIZABLE)

    return ventana