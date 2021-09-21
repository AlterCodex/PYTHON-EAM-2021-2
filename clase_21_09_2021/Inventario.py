from clase_21_09_2021.guitarra import Guitarra
class Inventario():

    def __init__(self):
        self.guitarras = []

    def agregar_guitarra(self,guitarra):
        if type(guitarra) == Guitarra:
            self.guitarras.append(guitarra)

    def buscar(self,marca):
        for g in self.guitarras:
            if g.marca == marca:
                yield g
