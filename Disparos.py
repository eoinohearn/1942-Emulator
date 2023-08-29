from lista_objetos import *
from Constantes import *

class bulletJugador:

    def __init__(self, x: int, y: int) -> None:
        '''Coloca el disparo del jugador'''
        self.x = x
        self.y = y
        self.w = 1
        self.h = 4
        self.dy = -10
        self.dx = 0
        shot_bullet.lista.append(self)

    def draw(self) -> None:
        '''Dibuja el disparo'''
        pyxel.blt(self.x, self.y, 0, 48, 16, self.w, self.h, 0)

    def update(self) -> None:
        '''Mueva el disparo. Se quita de la lista cuando ha salido de la pantalla'''
        self.y += self.dy
        self.x += self.dx
        if self.y < -2:
            shot_bullet.popLeft()

class bulletEnemigo:

    def __init__(self, x: int, y: int, avionX: int, avionY: int) -> None:
        '''Coloca el disparo del enemigo y crea una lénea entre el avion del jugador y el disparo. El disparo del enemigo sigue esta línea. Es
        como un vector.'''
        self.x = x
        self.y = y
        self.w = 4
        self.h = 4
        self.avionX = avionX
        self.avionY = avionY
        self.distance = (((self.x-self.avionX) ** 2) + ((self.y-self.avionY) ** 2)) ** 0.5
        self.dy = (self.avionY - self.y)/self.distance
        self.dx = (self.avionX - self.x)/self.distance
        shot_bullet_enemigos.lista.append(self)

    def draw(self) -> None:
        '''Dibuja el disparo'''
        pyxel.blt(self.x, self.y, 0, 51, 16, self.w, self.h, 0)

    def update(self) -> None:
        '''Mueva el disparo y comprube si ha salido de la pantalla'''
        self.y += 2 * self.dy
        self.x += 2 * self.dx
        if self.y > HEIGHT:
            shot_bullet_enemigos.lista.remove(self)

class bulletBombaderoSuper:

    def __init__(self, x: int, y: int, dx: int) -> None:
        '''Crea el disparo del bombadero super, y recibe como parámetro dx, que hace posible cambiar la dirreción en que mueva el disparo'''
        self.x = x
        self.y = y
        self.w = 4
        self.h = 4
        self.dy = 2
        self.dx = -2  + dx
        shot_bullet_enemigos.lista.append(self)

    def draw(self) -> None:
        '''Dibuja el disparo'''
        pyxel.blt(self.x, self.y, 0, 51, 16, self.w, self.h, 0)

    def update(self) -> None:
        '''Mueva el disparo y compruebe si ha salido de la pantalla'''
        self.x += 2 * self.dx
        self.y += 2 * self.dy
        if self.y > HEIGHT:
            shot_bullet_enemigos.lista.remove(self) 