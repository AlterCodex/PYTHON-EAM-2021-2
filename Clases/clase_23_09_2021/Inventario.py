from Clases.clase_23_09_2021.EspecificacionGuitarra import EspecificacionGuitarra
from Clases.clase_23_09_2021.guitarra import Guitarra
class Inventario():

    def __init__(self):
        self.guitarras = []

    def agregar_guitarra(self,guitarra):
        if type(guitarra) == Guitarra:
            espec = EspecificacionGuitarra()
            espec.agregar_parametro('serial', guitarra.serial)
            if len(list(self.buscar(espec))) == 0:
                self.guitarras.append(guitarra)
            else:
                raise Exception('Guitarra repetida')

    def buscar(self,especificacion):
        for g in self.guitarras:
            if g.cumple(especificacion):
                yield g

