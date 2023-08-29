from Blast import *
class bombadero: 

    def __init__(self) -> None:
        '''Crea las variables por el bombadero'''
        self.x = random.randint(0, HEIGHT/2)
        self.y = random.randint(-30, -10)
        self.w = 16
        self.h = 16
        self.dx = 0
        self.dy = 2
        self.yLímite = random.uniform(5*(HEIGHT/9), 6*(HEIGHT/9))
        self.xLímite = random.uniform(7*(WIDTH/9), 8*(WIDTH/9))
        lista_bombaderos.lista.append(self)
        self.reloj = pyxel.frame_count
        self.vidas = 5
        self.girandoPrimero = False
        self.grados = 0
        self.v = 0
        self.flipH = 1

    def draw(self) -> None:
        '''Dibuja el bombadero'''
        pyxel.blt(self.x, self.y, 0, 48, self.v, self.w, self.h * self.flipH, 0)



    def update(self) -> None:
        '''Mueva el bombadero, hace la gira, y compruebe si ha salido de pantalla o si ha muerto'''
        self.x += self.dx
        self.y += self.dy
        if self.y >= self.yLímite and not self.girandoPrimero:
            self.dy = 0
            self.dx = 2
            self.girarPrimero()
        if self.y <= -8 and self.girandoPrimero:
            lista_bombaderos.lista.remove(self)
        if self.vidas <= 0:
            lista_bombaderos.lista.remove(self)
            Blast(self.x+8, self.y+8)

        if self.grados == 45:
            self.v = 64
            if (pyxel.frame_count - self.relojGirar) >= 4:
                self.grados = 90
                self.relojGirar = pyxel.frame_count
        elif self.grados == 90:
            self.v = 48
            if self.x >= self.xLímite:
                self.dy = -2
                self.dx = 0
                self.grados = 135
                self.relojGirar = pyxel.frame_count
        elif self.grados == 135:
            self.v = 64
            self.flipH = -1
            if (pyxel.frame_count - self.relojGirar) >= 4:
                self.grados = 180
                self.relojGirar = pyxel.frame_count
                self.v = 0

    def girarPrimero(self) -> None:
        self.girandoPrimero = True
        self.grados = 45
        self.relojGirar = pyxel.frame_count
