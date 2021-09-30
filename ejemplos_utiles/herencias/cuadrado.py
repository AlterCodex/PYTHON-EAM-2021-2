from ejemplos_utiles.herencias.figura_geometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica):

    def __init__(self, lado):
        self.lado = lado
        super().__init__(lado ** 2)

    def perimetro(self):
        return self.lado+self.lado+self.lado+self.lado