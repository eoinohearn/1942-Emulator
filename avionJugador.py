from Disparos import *
class avionJugador:



    def __init__(self, x: int, y: int) -> None:
        '''Este métedo crea todas las variable necesarias por el avión del jugador'''
        self.x = x
        self.y = y
        self.w = 16
        self.h = 16
        self.vidas = 3
        self.bullet_limit = 3 #Esto es el límite de disparos que pueden aparecerse en la pantalla
        self.bullet_multiplier = 2
        self.girando = False
        self.grados = 0
        self.v = 0
        self.flip = 1
        self.velocidad = 3.5
        self.god_mode = False

    def draw(self) -> None:
        '''Dibuja el avión'''
        pyxel.blt(self.x, self.y, 0, 0, self.v, self.w, self.h * self.flip, 0)
        if not self.girando:
            pyxel.line(self.x+2 + 6 * (pyxel.frame_count // 3 % 2), self.y + 2, self.x + 7 + 6 * (pyxel.frame_count // 3 % 2), self.y + 2, 7)


    def update(self) -> None:
        '''Hace posible mover el avión, girar, y los dibujos cuando está girando'''
        if self.x+20 <= WIDTH:
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.x += self.velocidad
        if self.x-1 >= 0:
            if pyxel.btn(pyxel.KEY_LEFT):
                self.x -= self.velocidad
        if self.y >= 0:
            if pyxel.btn(pyxel.KEY_UP):
                self.y -= self.velocidad
        if self.y+17 <= HEIGHT:
            if pyxel.btn(pyxel.KEY_DOWN):
                self.y += self.velocidad

        if pyxel.btnp(pyxel.KEY_Z) and self.girando == False:
            self.girar()

        if self.grados == 45:
            self.y -= 3
            self.v = 48
            if (pyxel.frame_count - self.reloj) >= 5:
                self.grados = 90
                self.reloj = pyxel.frame_count
        elif self.grados == 90:
            self.y -= 1
            self.v = 64
            if pyxel.frame_count - self.reloj >= 5:
                self.grados = 135
                self.reloj = pyxel.frame_count
        elif self.grados ==135:
            self.y += 3
            self.v = 48
            self.flip = -1
            if pyxel.frame_count - self.reloj >= 5:
                self.grados = 180
                self.reloj = pyxel.frame_count
        elif self.grados == 180:
            self.y += 3
            self.v = 0
            if pyxel.frame_count - self.reloj >= 5:
                self.grados = 225
                self.reloj = pyxel.frame_count
        elif self.grados == 225:
            self.y += 3
            self.v = 48
            if pyxel.frame_count - self.reloj >= 5:
                self.grados = 270
                self.reloj = pyxel.frame_count
        elif self.grados == 270:
            self.y += 1
            self.v = 64
            if pyxel.frame_count - self.reloj >= 5:
                self.grados = 315
                self.reloj = pyxel.frame_count
        elif self.grados == 315:
            self.y -= 3
            self.v = 48
            self.flip = 1
            if pyxel.frame_count - self.reloj >= 5:
                self.grados = 360
                self.reloj = pyxel.frame_count
        elif self.grados == 360:
            self.y -= 3
            self.v = 0
            if pyxel.frame_count - self.reloj >= 4:
                self.grados = 0
                self.girando = False

    def girar(self) -> None:
        '''Empieza la gira del avión'''
        self.girando = True
        self.reloj = pyxel.frame_count
        self.grados = 45

    def avionShoot(self) -> None:
        '''Hace posible que el avión puede disparar'''

        if self.god_mode:
            self.bullet_limit = 1000000
            self.bullet_multiplier = 6
            self.velocidad = 8

            if len(shot_bullet.lista) < self.bullet_limit * self.bullet_multiplier:
                if pyxel.btn(pyxel.KEY_X):  #si uso btn puede pulsar el boton 'z' sin dejarlo, btnp hay que pulsar lo cada vez
                    for i in range(self.bullet_multiplier):
                        seperación = (i+1)*(self.w // (self.bullet_multiplier+1))
                        bulletJugador(self.x + seperación, self.y + 2)
        else:
            if len(shot_bullet.lista) < self.bullet_limit * self.bullet_multiplier:
                if pyxel.btnp(pyxel.KEY_X):  #si uso btn puede pulsar el boton 'z' sin dejarlo, btnp hay que pulsar lo cada vez
                    for i in range(self.bullet_multiplier):
                        seperación = (i+1)*(self.w // (self.bullet_multiplier+1))
                        bulletJugador(self.x + seperación, self.y + 2)