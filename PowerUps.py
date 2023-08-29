from lista_objetos import *
from Constantes import *
class VidaExtra:
    def __init__(self, x: int, y: int) -> None:
        '''Hace un power-up VidaExtra, que da el jugador una vida'''
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
        lista_vidasExtras.lista.append(self)

    def update(self) -> None:
        '''Mueva el power-up hasta que salga de la pantalla'''
        self.y += 1
        if self.y >= HEIGHT:
            lista_vidasExtras.lista.remove(self)

    def draw(self) -> None:
        '''Dibjua el power-up'''
        pyxel.blt(self.x, self.y, 0, 48, 24, self.w, self.h, 0)

class MásDisparos:
    def __init__(self, x: int, y: int) -> None:
        '''Hace un power-up que da más disparos al avión del jugador. Empieza a dos y va hasta seis'''
        self.x = x
        self.y = y
        self.w = 9
        self.h = 9
        lista_másDisparos.lista.append(self)

    def update(self) -> None:
        '''Mueva el power-up hasta que salga de la pantalla, y se quita de la lista'''
        self.y += 1
        if self.y >= HEIGHT:
            lista_másDisparos.lista.remove(self)

    def draw(self) -> None:
        '''Dibuja el power-up'''
        pyxel.blt(self.x, self.y, 0, 56, 24, self.w, self.h, 0)

lista_powerUps_tipos = [VidaExtra, MásDisparos]
