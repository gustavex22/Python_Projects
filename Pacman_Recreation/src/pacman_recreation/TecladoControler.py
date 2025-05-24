import pygame


def Identifier_Exit(run,event):

            
    #*Evento salir
    if event.type == pygame.QUIT:
        run = False
    else:
        run= True       
                
    return run
    

def Identifier_Key(event,Option):
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


def Update_Movement(PX,PY,Option,Velocidad,player):
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
        return PX,PY