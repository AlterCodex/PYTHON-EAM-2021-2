from Clases.clase_21_09_2021.guitarra import Guitarra
from Clases.clase_21_09_2021.Inventario import Inventario
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
    result= inventario.buscar(marca, modelo, '123465789', color, madera_mastil)
    print(list(result))
    inventario.agregar_guitarra('VIOLIN')
    print(inventario.guitarras)

    





