from lista_objetos import *
from Constantes import *
class Blast:
    def __init__(self, x: int, y: int) -> None:
        '''Crea el blast cuando se destruyen los aviones del juego'''
        self.x = x
        self.y = y
        self.radius = 8
        blasts_actual.lista.append(self)

    def update(self) -> None:
        '''El radius se suma hasta el límite, y se quita de la lista'''
        self.radius += 1
        if self.radius > 14:
            blasts_actual.lista.remove(self)

    def draw(self) -> None:
        '''Dibuja el blast'''
        pyxel.circ(self.x, self.y, self.radius, 7)
        pyxel.circb(self.x, self.y, self.radius, 10)