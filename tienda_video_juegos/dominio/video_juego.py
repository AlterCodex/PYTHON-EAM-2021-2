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
        self.id=None



    def _actualizar(self, id):
        from tienda_video_juegos.infraestructura.persistencia_videojuego import \
            PersistenciaVideoJuego
        persitencia_videoJuego = PersistenciaVideoJuego()
        persitencia_videoJuego.actualizar(self,id)


    def _guardar(self ,serial):
        from tienda_video_juegos.infraestructura.persistencia_videojuego import \
            PersistenciaVideoJuego
        persitencia_videoJuego=PersistenciaVideoJuego()
        persitencia_videoJuego.guardar(self, serial)

    def guardar(self):
        if self.id is None:
            self._guardar(self.serial)
        else:
            self._actualizar(self.id)



    def update(self, dict_params):
        self.nombre = dict_params.get('nombre', self.nombre)
        self.release_date = dict_params.get('release_date', self.release_date)
        self.clasificacion=dict_params.get('clasificacion', self.clasificacion)
        self.consola = dict_params.get('consola', self.consola)
        self.empresa = dict_params.get('empresa', self.empresa)
        self.numero_jugadores = dict_params.get('numero_jugadores', self.numero_jugadores)
        self.tipo_juego = dict_params.get('tipo_juego', self.tipo_juego)
        self.serial=dict_params.get('serial', self.serial)

