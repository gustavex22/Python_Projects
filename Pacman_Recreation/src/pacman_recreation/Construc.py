import pygame


class Muro():
    
    def __init__(self,X,Y):
        Ancho = 200
        Alto = 100
        
        self.forma = pygame.Rect(0,0,Alto,Ancho)
        self.forma.center = (X,Y)
        
    def drawEstructure(self,ventana,Color):
        pygame.draw.rect(ventana,Color,self.forma,0)
        pygame.draw.rect(ventana,(0,0,47),self.forma,3)
