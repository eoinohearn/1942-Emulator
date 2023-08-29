from Blast import *
from PowerUps import *
class enemigoRojo:


    def __init__(self, x: int, y: int) -> None:
        '''Crea todas las variables del enemigoRojo'''
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16
        self.grados = 0
        self.girando = False
        self.dx = 3
        self.vidas = 1
        self.v = 0
        self.flipH = 1
        self.flipW = 1
        lista_enemigos_rojos.lista.append(self)

    def draw(self) -> None:
        '''Dibuja el enemigo rojo'''
        pyxel.blt(self.x, self.y, 0, 32, self.v, self.w * self.flipW, self.h * self.flipH, 0)
        

    def update(self) -> None:
        '''Mueva el enemigo rojo y compruebe si ha salido de la pantalla o si ha muerto. Tambíen hace la gira'''
        self.x += self.dx
        if self.x >= WIDTH:
            lista_enemigos_rojos.lista.remove(self)
        if self.x >= WIDTH/2 and self.girando == False:
            self.girar()
        if self.vidas <= 0:
            Blast(self.x+8, self.y+8)
            intento = random.random()
            intento2 = random.random()
            if intento <= VIDAS_EXTRA_CASUALIDAD:
                lista_powerUps_tipos[0](self.x, self.y)
            if intento2 <= DISPAROS_MULTIPLICADO_CASUALIDAD:
                lista_powerUps_tipos[1](self.x, self.y)
            lista_enemigos_rojos.lista.remove(self)

        if self.grados == 45:
            self.y += 3
            self.v = 48
            if (pyxel.frame_count - self.reloj) >= 4:
                self.grados = 90
                self.reloj = pyxel.frame_count
        elif self.grados == 90:
            self.y += 3
            self.v = 32
            if (pyxel.frame_count - self.reloj) >= 4:
                self.dx *= -1
                self.grados = 135
                self.reloj = pyxel.frame_count
        elif self.grados == 135:
            self.y += 3
            self.v = 48
            self.flipW = -1
            if (pyxel.frame_count - self.reloj) >= 4:
                self.grados = 180
                self.reloj = pyxel.frame_count
        elif self.grados == 180:
            self.v = 0
            if (pyxel.frame_count - self.reloj) >= 4:
                self.grados = 225
                self.reloj = pyxel.frame_count
        elif self.grados == 225:
            self.y -= 3
            self.v = 48
            self.flipH = -1
            if (pyxel.frame_count - self.reloj) >= 4:
                self.grados = 270
                self.reloj = pyxel.frame_count
        elif self.grados == 270:
            self.y -=3
            self.v = 32
            self.flipW = 1
            if (pyxel.frame_count - self.reloj) >= 4:
                self.dx *= -1
                self.grados = 315
                self.reloj = pyxel.frame_count
        elif self.grados == 315:
            self.y -=3
            self.v = 48
            if (pyxel.frame_count - self.reloj) >= 4:
                self.grados = 0
                self.v = 0
                self.flipH = 1
                self.flipW = 1

                

    def girar(self) -> None:
        '''Empieza la gira'''
        self.girando = True
        self.reloj = pyxel.frame_count
        self.grados = 45