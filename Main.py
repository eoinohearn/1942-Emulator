# Hecho por Eoin O'Hearn. 12.11.2022
from Objetos import *
from avionJugador import *


class app:

    
    def __init__(self) -> None:
        '''Cuando llamas un objeto de tipo App, este método se hace. Crea el avión del jugador y dos 
        variables, game_playing y pantalla'''
        self.game_playing = True
        self.avion = avionJugador(WIDTH/2 - 8, HEIGHT - 32)
        self.pantalla = 'Inicio'
        pyxel.run(self.update, self.draw)


    def update(self) -> None:
        '''Mientras se juega el juego este métedo se llama, actualizando todo los otros objetos. Todo la logíca 
        esta dentro de este métedo'''
        if self.pantalla == 'Inicio':
            self.pantalla_Inicio_Update()
        elif self.pantalla == 'Jugando':
            if self.game_playing:
                self.avion.update()
                self.avion.avionShoot()
                self.enemigoShoot()
                enemigos_vivos.update()
                shot_bullet.update()
                shot_bullet_enemigos.update()
                blasts_actual.update()
                self.checkCollision()
                powerUps_actual.update()
                self.crearEnemigos()


        
    def draw(self) -> None:
        '''Este métedo es responsible por lo que se ve en la pantalla. Todos los dibujos pueden ser encontrados aquí'''
        if self.pantalla == 'Inicio':
            self.pantalla_Inicio_Draw()
        elif self.pantalla == 'Jugando':
            self.gameStatus()
            if self.game_playing:
                shot_bullet.draw()
                shot_bullet_enemigos.draw()
                enemigos_vivos.draw()
                self.avion.draw()
                blasts_actual.draw()
                powerUps_actual.draw()


    def pantalla_Inicio_Update(self) -> None:
        '''Este métedo se hace posible jugar el juego y no quedarse en la pantalla de inicio'''
        if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
        if pyxel.btnp(pyxel.KEY_E):
            self.pantalla = 'Jugando'
        if pyxel.btnp(pyxel.KEY_G):
            global ENEMIGO_CASUALIDAD, ENEMIGO_ROJO_CASUALIDAD, BOMBADERO_CASUALIDAD, BOMBADERO_SUPER_CASUALIDAD
            self.avion.god_mode = True
            ENEMIGO_CASUALIDAD = 0.02 * 3
            ENEMIGO_ROJO_CASUALIDAD = 0.01 * 3
            BOMBADERO_CASUALIDAD = 0.0075 * 3
            BOMBADERO_SUPER_CASUALIDAD = 0.005 * 3

        '''
        Aquí puedo cambiar los variables para modo God y cosas así
        '''


    def pantalla_Inicio_Draw(self) -> None:
        '''Este métedo dibuja la pantalla de inicio'''
        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,0, WIDTH, HEIGHT)
        pyxel.text(100, 20, '1942: Simulador', pyxel.frame_count // 3 % 16)
        pyxel.rect(64, 64, 24, 24, 0)
        pyxel.rect(64, 94, 24, 24, 0)
        pyxel.rect(64, 124, 24, 24, 0)
        pyxel.rect(64, 154, 24, 24, 0)
        pyxel.rect(64, 184, 24, 24, 0)
        pyxel.rect(90, 62, 120, 24, 0)
        pyxel.rect(90, 94, 120, 24, 0)
        pyxel.rect(90, 124, 120, 24, 0)
        pyxel.rect(90, 154, 120, 24, 0)
        pyxel.rect(90, 184, 120, 24, 0)
        pyxel.blt(68, 68, 0, 0, 0, 16, 16, 0)
        pyxel.text(92, 70, 'Jugador: Disparar X.', 2)
        pyxel.text(92, 76, 'Girar Z. Moverse Las Flechas', 2)
        pyxel.blt(68, 98, 0, 16, 0, 16, 16, 0)
        pyxel.text(92, 102, 'Enemigo: 5 puntos', 2)
        pyxel.blt(68, 128, 0, 32, 0, 16, 16, 0)
        pyxel.text(92, 132, 'Enemigo Rojo: 1 Punto', 2)
        pyxel.blt(68, 158, 0, 48, 0, 16, 16, 0)
        pyxel.text(92, 162, 'Bombadero: 20 Puntos', 2)
        pyxel.blt(68, 188, 0, 0, 16, 16, 16, 0)
        pyxel.text(92, 192, 'Bombadero Super: 50 Puntos', 2)
        pyxel.text(88, HEIGHT - 20, 'Pulsa E Para Empezar', pyxel.frame_count // 3 % 16)
        pyxel.text(88, HEIGHT - 10, 'Pulsa G Para Modo God', pyxel.frame_count // 3 % 16)
        if self.avion.god_mode:
            pyxel.text(88, HEIGHT - 10, 'Pulsa G Para Modo God', 11)

        



    def checkCollision(self) -> None:
        '''Este métedo compruebe todos las collisión que son posibles en el juego'''
        global score

        '''Este bucle compruebe la colisión entre los enemigos y los disparos del jugador'''
        for element in enemigos_vivos.lista:
            for i in element.lista:
                for j in shot_bullet.lista:
                    if self.isCollision(j.x, j.y, i.x+8, i.y+8):
                        i.vidas -= 1
                        if i.vidas == 0:
                            if type(i) == lista_enemigos_tipos[0]:
                                score += 5
                            elif type(i) == lista_enemigos_tipos[1]:
                                score += 1
                            elif type(i) == lista_enemigos_tipos[2]:
                                score += 20
                            elif type(i) == lista_enemigos_tipos[3]:
                                score += 50
                        shot_bullet.lista.remove(j)
                    

        '''Este bucle compruebe la colisón entre los disparos de los enemigos y el avion del jugador'''
        if not self.avion.god_mode:
            for i in shot_bullet_enemigos.lista:
                if self.isCollision(self.avion.x + 8, self.avion.y + 8, i.x+1, i.y+1) and self.avion.girando == False:
                    shot_bullet_enemigos.lista.remove(i)
                    self.avion.vidas -= 1
                    Blast(self.avion.x+8, self.avion.y+8)
                    self.gameReset()
                    if self.avion.vidas == 0:
                        self.game_playing = False
                    

        '''Este bucle compruebe la colisión entre los diparos de los enemigos y los disparos del jugador'''
        for i in shot_bullet.lista:
            for j in shot_bullet_enemigos.lista:
                if self.isCollision(i.x, i.y, j.x+1, j.y+1):
                    if i in shot_bullet.lista:
                        shot_bullet.lista.remove(i)
                    if j in shot_bullet_enemigos.lista:
                        shot_bullet_enemigos.lista.remove(j)

 
        '''Este bucle compruebe la colisión entre el avión del jugador y los aviones de los enemigos'''
        if not self.avion.god_mode:
            for element in enemigos_vivos.lista:
                for j in element.lista:
                    if self.isCollision(self.avion.x + 8, self.avion.y + 8, j.x + 8, j.y + 8) and self.avion.girando == False:
                        self.avion.vidas -= 1
                        j.vidas -= 1
                        Blast(self.avion.x+8, self.avion.y+8)
                        self.gameReset()
                        if self.avion.vidas == 0:
                            self.game_playing = False

        '''Este bucle comprube la colisión entre el avión del jugador y los Power-Ups'''
        for element in powerUps_actual.lista:
            for j in element.lista:
                if self.isCollision(self.avion.x + 8, self.avion.y + 8, j.x + 8, j.y + 8):
                    if type(j) == lista_powerUps_tipos[0]:
                        self.avion.vidas += 1
                    elif type(j) == lista_powerUps_tipos[1]:
                        if self.avion.bullet_limit < 8 and self.avion.bullet_multiplier < 5:
                            self.avion.bullet_multiplier += 1
                            self.avion.bullet_limit += 1
                    score += 100
                    element.lista.remove(j)

    def enemigoShoot(self) -> None:
        '''Este método hace posible que los enemigos pueden disparar al jugador. Tiene que estar aquí adentro de 
        la clase app porque se necesita la posición del jugador'''

        for element in enemigos_vivos.lista:
            for i in element.lista:
                if type(i) == lista_enemigos_tipos[0]:
                    if i.y >= i.yLímite/2 and i.shot == False:
                        bulletEnemigo(i.x + 4, i.y + 2, self.avion.x, self.avion.y)
                        i.shot = True
                elif type(i) == lista_enemigos_tipos[2]:
                    if pyxel.frame_count - i.reloj >= 60:
                        i.reloj = pyxel.frame_count
                        for j in range(2):
                            bulletEnemigo(i.x + 8, i.y + 8, self.avion.x, self.avion.y)

                elif type(i) == lista_enemigos_tipos[3]:
                    if pyxel.frame_count - i.reloj >= 60:
                        i.reloj = pyxel.frame_count
                        for j in range(5):
                            bulletBombaderoSuper(i.x + 8, i.y + 8, j)

    def crearEnemigos(self) -> None:
        '''Este métedo crea los enemigos aleatoriamente con la variable intento. Si este variable es igual o menos a 
        la casualidad de un tipo de enemigo, este tipo de enemigo se crea y se aparece en la pantalla.'''


        if pyxel.frame_count > 100:
            intento = random.random()
            if intento <= ENEMIGO_CASUALIDAD and len(lista_enemigos.lista) < 5:
                for i in range(random.randint(1,3)):
                    lista_enemigos_tipos[0]()

            if intento <= ENEMIGO_ROJO_CASUALIDAD and len(lista_enemigos_rojos.lista) < 5:
                y = random.randint(50,100)
                for i in range(random.randint(1,5)):
                    lista_enemigos_tipos[1](i * -16, y)

            if intento <= BOMBADERO_CASUALIDAD and len(lista_bombaderos.lista) == 0:
                lista_enemigos_tipos[2]()

            if intento <= BOMBADERO_SUPER_CASUALIDAD and len(lista_bombaderos_super.lista) == 0:
                lista_enemigos_tipos[3]()

    def isCollision(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        '''Este métedo usa la función de distancía para comprobar las colisiones en el juego. Si la distancía entre 
        dos objetos es menor de ocho, hay una colisión'''
        distancia = (((x1-x2) ** 2) + ((y1-y2) ** 2)) ** 0.5
        collision = False
        if distancia <= 8:
            collision = True
        return collision

    def gameStatus(self) -> None:
        '''Este métedo es responsible por la diferencía entre el juego y la pantalla cuando se muere el jugador'''
        global score
        if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
        if  self.game_playing:
            pyxel.cls(0)
            pyxel.bltm(0,0,0,0,-pyxel.frame_count%128, WIDTH, HEIGHT)
            pyxel.rect(0, 0, 50, 19, 0)
            pyxel.text(8, 3, f"Score: {score}", 2)
            pyxel.text(8, 10, f"Vidas: {self.avion.vidas - 1}", 2)
        else:
            pyxel.cls(0)
            pyxel.bltm(0,0,0,0,0, WIDTH, HEIGHT)
            pyxel.rect(WIDTH/2 - 70, HEIGHT/2 - 20, 140, 40, 0)
            pyxel.text(WIDTH/2 - 19, HEIGHT/2 - 7, 'GAME OVER', 2)
            pyxel.text(WIDTH/2 - 18, HEIGHT/2, f"Score: {score}", 2)
            pyxel.text(WIDTH/2 - 60, HEIGHT/2 + 7, "Pulsa R para intentar otra vez", 2)
            if pyxel.btnp(pyxel.KEY_R):
                self.gameReset()
                score = 0
                self.avion.vidas = 3
                self.game_playing = True

    def gameReset(self) -> None:
        '''Si el jugador quiere jugar otra vez despues de morir tres veces, este métedo cambia todo el juego para iniciarlo otra vez'''
        self.avion.x = WIDTH/2 - 8
        self.avion.y = HEIGHT -32
        self.avion.bullet_limit = 3
        self.avion.bullet_multiplier = 2
        for element in enemigos_vivos.lista:
            element.lista.clear()
        for element in powerUps_actual.lista:
            element.lista.clear()
        shot_bullet.lista.clear()
        shot_bullet_enemigos.lista.clear()




pyxel.init(WIDTH, HEIGHT, title =CAPTION)
pyxel.load("assets/assets.pyxres")
app() 

#display_scale=2

'''
Ideas










'''

