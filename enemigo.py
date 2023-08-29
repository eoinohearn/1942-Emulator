from Blast import *
class enemigo:

    def __init__(self) -> None:
        '''Crea todas las variables necesarias por el enemigo'''
        self.x = random.randint(0, WIDTH - 8)
        self.y = random.randint(-50, -8)
        self.w = 16
        self.h = 16
        self.xLímite = random.uniform(WIDTH/6, 5/6*(WIDTH))
        self.yLímite = random.uniform(7*(HEIGHT/9), 8*(HEIGHT/9))
        self.distance = (((self.x-self.xLímite) ** 2) + ((self.y-self.yLímite) ** 2)) ** 0.5
        self.dy = (self.yLímite - self.y)/self.distance
        self.dx = (self.xLímite - self.x)/self.distance
        self.girando = False
        self.grados = 0
        self.shot = False
        self.vidas = 1
        self.v = 0
        self.flip = 1
        lista_enemigos.lista.append(self)

    def draw(self) -> None:
        '''Dibuja el enemigo'''
        pyxel.blt(self.x, self.y, 0, 16, self.v, self.w, self.h * self.flip, 0)

    
    def update(self) -> None:
        '''Mueva el enemigo y compruebe si ha salido de la pantalla o si ha muerto'''
        self.y += 3 * self.dy
        self.x += 3 * self.dx
        if self.y <= -8 and self.girando:
            lista_enemigos.lista.remove(self)
        elif self.vidas <= 0:
            lista_enemigos.lista.remove(self)
            Blast(self.x+8, self.y+8)

        if self.y >= self.yLímite:
            self.girar()

        if self.grados == 45:
            self.v = 32
            if (pyxel.frame_count - self.reloj) >= 3:
                self.grados = 90
                self.reloj = pyxel.frame_count
        elif self.grados == 90:
            self.v = 48
            if pyxel.frame_count - self.reloj >= 3:
                self.grados = 135
                self.reloj = pyxel.frame_count
        elif self.grados ==135:
            self.v = 32
            self.flip = -1
            if pyxel.frame_count - self.reloj >= 3:
                self.grados = 0
                self.v = 0
        
            

    def girar(self) -> None:
        '''Empieza la gira'''
        self.girando = True
        self.reloj = pyxel.frame_count
        self.dy = -1
        self.grados = 45