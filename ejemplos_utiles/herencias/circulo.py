from ejemplos_utiles.herencias.figura_geometrica import FiguraGeometrica
import math


class Circulo(FiguraGeometrica):

    def __init__(self, radio):
        super().__init__(math.pi * (radio ** 2))
        self.radio = radio


    def perimetro(self):
        return self.radio*2*math.pi