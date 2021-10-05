from Clases.clase_23_09_2021.EspecificacionGuitarra import EspecificacionGuitarra
from Clases.clase_23_09_2021.Inventario import  Inventario
from Clases.clase_23_09_2021.guitarra import Guitarra
import random
def test_buscar():
    marcas= ['fender','guibson','artesanal']
    modelos = {
            'fender':['f1','f2','f3','f4'],
            'guibson':['G1','G2','G3','G4'],
            'artesanal':['a1']
    }
    inv = Inventario()
    for marca in marcas:
        for modelo in modelos[marca]:
            inv.agregar_guitarra(
                Guitarra('ROJA', modelo,marca)
            )
    especificacion = EspecificacionGuitarra()
    especificacion.agregar_parametro('marca','fender')
    for guitarra in inv.buscar(especificacion):
        assert guitarra is not None
    assert len(list(inv.buscar(especificacion)))>0



def test_fuzzing_buscar():
    marcas= ['fender','guibson','artesanal']
    modelos = {
            'fender':['f1','f2','f3','f4'],
            'guibson':['G1','G2','G3','G4'],
            'artesanal':['a1']
    }
    colores =['Azul','Rojo','Verde','Naranja','Amarillo','Cafe','Blanco','Negro']
    maderas = ['balso','triplex','pino','roble','mata raton', 'caoba']
    cantidad_guitarras= random.randint(100,1000)
    inventario=Inventario()
    especificaciones = []
    for i in range(cantidad_guitarras):
        marca = random.choice(marcas)
        modelo = random.choice(modelos[marca])
        color = random.choice(colores)
        madera_mastil = random.choice(maderas)
        madera_diapason = random.choice(maderas)
        if i%10==0:
            especificacion = EspecificacionGuitarra()
            especificacion.agregar_parametro('marca',marca)
            especificacion.agregar_parametro('modelo',modelo)
            especificaciones.append(especificacion)
        g = Guitarra(color,modelo,marca,madera_mastil,madera_diapason)
        inventario.agregar_guitarra(g)
    cantidad_busquedas= random.randint(1,len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar(esp))) > 0
        print('encontradas:')
        print(list(inventario.buscar(esp)))
    esp_fake= EspecificacionGuitarra()
    esp_fake.agregar_parametro('clavijas','doradas')
    print(inventario.guitarras)
    assert len(list(inventario.buscar(esp_fake))) == 0
    g = Guitarra(color, modelo, marca, madera_mastil, madera_diapason)
    inventario.agregar_guitarra(g)
    try:
        inventario.agregar_guitarra(g)
        assert False
    except Exception as ex:
        assert  ex;

if __name__ == '__main__':
    test_fuzzing_buscar()