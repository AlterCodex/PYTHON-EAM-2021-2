from clase_28_09_2021.Dominio.Inventario import Inventario
from clase_28_09_2021.Dominio.guitarra import Guitarra
from clase_28_09_2021.Infraestructura.PersistenciaGuitarra import PersistenciaGuitarra

inventario=Inventario()
import random
import os

if __name__== '__main__':
    saver = PersistenciaGuitarra()
    saver.connect()
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
    PersistenciaGuitarra.save(g)
    PersistenciaGuitarra.save_json(g)
    inventario = Inventario()
    inventario_json=Inventario()
    for file in os.listdir("./files"):
        if '.gui' in file:
            inventario.agregar_guitarra(PersistenciaGuitarra.load(file))
        if '.json' in file:
            inventario_json.agregar_guitarra(PersistenciaGuitarra.load_json(file))
    for g in inventario.guitarras:
        g.pintar("morado")
        saver.guardar_guitarra(g)
        PersistenciaGuitarra.save(g)
        PersistenciaGuitarra.save_json(g)





    





