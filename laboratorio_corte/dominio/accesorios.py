from laboratorio_corte.dominio.articulo import Articulo


class Accesorios(Articulo):

    def __init__(self):
        self.nombre= ''
        self.proveedor = ''
        self.modelo = ''
        self.marca = ''
        self.color = ''
        self.consolas_compatibles = []
        self.size = ''