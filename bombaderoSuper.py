from Blast import *
class bombaderoSuper:

    def __init__(self) -> None:
        '''Crea todas las variables del bombadero super'''
        self.x = random.randint(0, WIDTH - 16)
        self.y = random.randint(HEIGHT + 10, HEIGHT + 40)
        self.w = 16
        self.h = 16
        self.dy = -1
        lista_bombaderos_super.lista.append(self)
        self.reloj = pyxel.frame_count
        self.vidas = 20

    def draw(self) -> None:
        '''Dibuja el bombadero super'''
        pyxel.blt(self.x, self.y, 0, 0, 16, self.w, -self.h, 0)

    def update(self) -> None:
        '''Mueva el bombadero super y compruebe si ha salido de pantalla o si ha muerto'''
        self.y += self.dy
        if self.y <= -16:
            lista_bombaderos_super.lista.remove(self)
        if self.vidas <= 0:
            lista_bombaderos_super.lista.remove(self)
            Blast(self.x+8, self.y+8)