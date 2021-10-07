from laboratorio_corte.dominio.articulo import Articulo
from laboratorio_corte.infraestructura.persistencia_videojuego import PersistenciaVideoJuego

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
        persitencia_videoJuego=PersistenciaVideoJuego()
        persitencia_videoJuego.connect()
        persitencia_videoJuego.guardar(self, serial)
