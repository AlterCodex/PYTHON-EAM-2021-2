from laboratorio_corte.dominio.articulo import Articulo


class Consola(Articulo):

    def __init__(self):
        self.nombre = ''
        self.numero_controles=''
        self.modelo = ''
        self.fabricante = ''
        self.accesorios = []
        self.color = ''
        self.size = ''