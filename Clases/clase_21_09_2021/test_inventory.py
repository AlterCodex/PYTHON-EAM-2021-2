from Clases.clase_21_09_2021.Inventario import Inventario
from Clases.clase_21_09_2021.guitarra import Guitarra

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
    assert True

if __name__ == '__main__':
    test_buscar()