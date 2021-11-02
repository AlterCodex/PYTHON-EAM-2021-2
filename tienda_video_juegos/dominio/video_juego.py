from tienda_video_juegos.dominio.articulo import Articulo


class VideoJuego(Articulo):




    def __init__(self,nombre,release_date,clasificacion,consola,
                 empresa, numero_jugadores,tipo_juego,serial,**kargs):
        self.nombre = nombre
        self.release_date = release_date
        self.clasificacion=clasificacion
        self.consola = consola
        self.empresa = empresa
        self.numero_jugadores = numero_jugadores
        self.tipo_juego = tipo_juego
        self.serial=serial



    def _guardar(self ,serial):
        from tienda_video_juegos.infraestructura.persistencia_videojuego import \
            PersistenciaVideoJuego
        persitencia_videoJuego=PersistenciaVideoJuego()
        persitencia_videoJuego.guardar(self, serial)

    def guardar(self):
        self._guardar(self.serial)