import pygame
import Option

class Personaje():
    
    def __init__(self,x,y):
        Ancho= Option.Ancho_jugador
        Alto = Option.Altura_jugador
        self.Radio =Ancho//2
        self.Center = (x,y)
        self.forma = pygame.Rect(0,0,Ancho,Alto)
        self .forma.center= self.Center
        
    def Movimiento(self,PX,PY):
        self.forma.x +=PX
        self.forma.y+=PY
        self.Center=self.forma.center
    
        
    def draw(self,Interfaz):
        self.forma = pygame.draw.circle(
            Interfaz , 
            Option.ColorPersonaje ,
            self.Center ,  
            self.Radio)
        