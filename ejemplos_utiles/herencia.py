import math

from ejemplos_utiles.herencias.circulo import Circulo
from ejemplos_utiles.herencias.cuadrado import Cuadrado
from ejemplos_utiles.herencias.figura_geometrica import FiguraGeometrica


if __name__ == '__main__':
    figuras =[]
    figuras.append(Circulo(10))
    figuras.append(Cuadrado(7))
    print(Circulo.__bases__)
    print(Cuadrado.__bases__)
    print(FiguraGeometrica.__subclasses__())
    for i in figuras:
        print(i)
        print(f'el perimetro es: {i.perimetro()}')
        if isinstance(i, FiguraGeometrica):
            print(f'El {type(i)} es una figura geometrica')
        if isinstance(i, Cuadrado):
            print(f"{i} es un Cuadrado")

