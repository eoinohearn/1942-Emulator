class lista_objetos:

    def __init__(self) -> None:
        '''Hace una lista'''
        self.lista = []

    def popLeft(self) -> None:
        '''Se quite el elemento en la posición [0]'''
        self.lista = self.lista[1:]

    def draw(self) -> None:
        '''Itera por la lista y llama el métedo draw de cada elemento'''
        for j in self.lista:
            j.draw()

    def update(self) -> None:
        '''itera por la lista y llama el métedo update de cada elemento'''
        for j in self.lista:
            j.update()

enemigos_vivos = lista_objetos()
powerUps_actual = lista_objetos()

lista_enemigos = lista_objetos()
lista_enemigos_rojos = lista_objetos()
lista_bombaderos = lista_objetos()
lista_bombaderos_super = lista_objetos()

shot_bullet = lista_objetos()
blasts_actual = lista_objetos()
shot_bullet_enemigos = lista_objetos()

lista_vidasExtras = lista_objetos()
lista_másDisparos = lista_objetos()