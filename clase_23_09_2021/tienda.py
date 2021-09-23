from clase_23_09_2021.guitarra import Guitarra
from clase_23_09_2021.Inventario import Inventario

inventario=Inventario()

if __name__== '__main__':
    color = str(input('ingrese el color:'))
    modelo = str(input('ingrese el Modelo:'))
    marca = str(input('ingrese la marca:'))

    madera_mastil = str(input('ingrese la madera del mastil:'))
    madera_diapason = str(input('ingrese la madera del mastil:'))

    guitarra = Guitarra(color, modelo, marca,
                 madera_mastil, madera_diapason)
    inventario.agregar_guitarra(guitarra)
    print(inventario.guitarras)
    inventario.agregar_guitarra('VIOLIN')
    print(inventario.guitarras)

    





