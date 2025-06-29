import pygame

class pacman:
        def __init__(self, x, y, options):
            Ancho = options.Ancho_jugador
            Altura = options.Altura_jugador

            self.radio = Ancho // 2
            self.Center = (x, y)
            self.forma = pygame.Rect(0, 0, Ancho, Altura)
            self.forma.center = self.Center


        def Movimiento(self, PX, PY,option):
            self.forma.x += PX
            self.forma.y += PY

            TOP_left = self.forma.left
            TOP_right =self.forma.right
            TOP_down =self.forma.top
            TOP_up =self.forma.bottom

            # Limitar dentro de la ventana
            if TOP_left < 0:
                self.forma.left = 0

            if TOP_right > option.Ancho:
                self.forma.right = option.Ancho

            if TOP_down < 0:
                self.forma.top = 0

            if TOP_up > option.Altura:
                self.forma.bottom = option.Altura

            self.Center = self.forma.center


        def draw(self, Interfaz,options):
                self.forma.center = self.Center  # Actualiza la forma del jugador con el centro actualizado
                pygame.draw.circle(
                Interfaz,
                options.ColorPersonaje,
                self.Center,
                self.radio
                )
