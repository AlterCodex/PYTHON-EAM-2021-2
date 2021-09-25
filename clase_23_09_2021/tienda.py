from clase_23_09_2021.guitarra import Guitarra
from clase_23_09_2021.Inventario import Inventario
from clase_23_09_2021.EspecificacionGuitarra import EspecificacionGuitarra
inventario=Inventario()
import random
import os

if __name__== '__main__':
    marcas= ['fender','guibson','artesanal']
    modelos = {
            'fender':['f1','f2','f3','f4'],
            'guibson':['G1','G2','G3','G4'],
            'artesanal':['a1']
    }
    colores =['Azul','Rojo','Verde','Naranja','Amarillo','Cafe','Blanco','Negro']
    maderas = ['balso','triplex','pino','roble','mata raton', 'caoba']
    marca = random.choice(marcas)
    modelo = random.choice(modelos[marca])
    color = random.choice(colores)
    madera_mastil = random.choice(maderas)
    madera_diapason = random.choice(maderas)
    g = Guitarra(color, modelo, marca, madera_mastil, madera_diapason)
    Guitarra.save(g)
    Guitarra.save_json(g)
    inventario = Inventario()
    inventario_json=Inventario()
    for file in os.listdir():
        if '.gui' in file:
            inventario.agregar_guitarra(Guitarra.load(file))
        if '.json' in file:
            inventario_json.agregar_guitarra(Guitarra.load_json(file))
    print(inventario.guitarras)
    print(inventario_json.guitarras)



    





