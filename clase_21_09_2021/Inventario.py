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

    def buscar(self,marca, modelo, serial, color, madera):
        for g in self.guitarras:
            if g.marca == marca and g.modelo == modelo\
                    and g.serial == serial and g.color ==color \
                    and (g.madera_del_mastil== madera or g.madera_del_diapason==madera):
                yield g