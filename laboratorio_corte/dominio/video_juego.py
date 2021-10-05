from laboratorio_corte.dominio.articulo import Articulo


class VideoJuego(Articulo):

    def __init__(self):
        self.nombre = ''
        self.release_date = ''
        self.clasificacion=''
        self.consola = ''
        self.empresa = ''
        self.numero_jugadores = ''
        self.tipo_juego = ''


    def guardar(self ,serial):
