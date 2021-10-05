from laboratorio_corte.dominio.articulo import Articulo


class Producto(Articulo):


    def __init__(self):
        self.serial = None
        #algo del mundo real (Video Juego, Consola, Camiseta)
        self.articulo = None
        self.precio = 0
        self.iva = 0
        self.garantia_meses = 3
        self.tipo = None
        self.cantidad_disponible = 0
        self.prendido = False
