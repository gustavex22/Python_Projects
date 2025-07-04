import pygame

def Tecla_Exit(run , event): #? Identifica si el evento salir se cumple

    # Evento Salir
    if event.type == pygame.QUIT:
        run = False
    else:
        run = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F4 and (event.mod & pygame.KMOD_ALT):
            run = False

    return run


def Tecla_Identity(event,Option,ventana):#? Identifica que tecla se ha presionado y actualiza las opciones de movimiento
    fullscreen = ventana.get_flags() & pygame.FULLSCREEN


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            Option.M_Izquierda = True
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            Option.M_Derecha = True
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            Option.M_Atras = True
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            Option.M_Arriba = True

    #! Este bloque de codigo es para cuando se deja de tocar una tecla, es opcional codificarlo
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            Option.M_Izquierda = False
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            Option.M_Derecha = False
        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            Option.M_Atras = False
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            Option.M_Arriba = False




def Update_Movement(PX, PY, Option, Velocidad, player):
    # ? Sentencias If de movimiento

    if Option.M_Izquierda == True:
        PX -= Velocidad
    if Option.M_Derecha == True:
        PX += Velocidad
    if Option.M_Arriba == True:
        PY -= Velocidad
    if Option.M_Atras == True:
        PY += Velocidad

    player.Movimiento(PX, PY, Option)  # ?Actualiza el movimiento del jugador
    return PX, PY