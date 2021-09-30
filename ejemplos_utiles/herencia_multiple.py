from ejemplos_utiles.herencias.circulo import Circulo
from ejemplos_utiles.herencias.figura_geometrica import FiguraGeometrica
from ejemplos_utiles.herencias.llanta import LLanta


class LLantaBici(LLanta,Circulo):

    presionMaxima=100

    def __init__(self,rin):
        Circulo.__init__(self,rin)
        LLanta.__init__(self,rin,0)


    def inflar(self, presion_nueva):
        if(presion_nueva > LLantaBici.presionMaxima):
            print("BUM exploto la rueda")
        else:
            super(LLantaBici, self).inflar(presion_nueva)


if __name__ == '__main__':
    llanta = LLantaBici(10)
    print(llanta)
    print(LLantaBici.__bases__)
    if isinstance(llanta,LLanta):
        print('Es una LLanta')
        llanta.inflar(150)
    if isinstance(llanta,Circulo):
        print(f"Circular de perimetro: {llanta.perimetro()}")
    if isinstance(llanta,FiguraGeometrica):
        print(f"Ademas es una Figura Geometrica  de area{llanta.area}")
