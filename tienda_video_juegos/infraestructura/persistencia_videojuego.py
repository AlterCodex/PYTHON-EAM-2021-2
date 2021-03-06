import sqlite3


class PersistenciaVideoJuego():

    def __init__(self):
        self.connect()

    def connect(self):
        self.con = sqlite3.connect("la_tienda_de_los_nerds.sqlite")
        print(self.con.cursor())
        self.__crear_tabla()

    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE " \
                    "VideoJuego(" \
                    "id Integer PRIMARY KEY Autoincrement," \
                    "nombre Text," \
                    "release_date text," \
                    "clasificacion text, " \
                    "consola text," \
                    "empresa text," \
                    "numero_jugadores integer ," \
                    "tipo_juego text," \
                    "serial text," \
                    "FOREIGN KEY(serial) references Producto(serial))"
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar(self, videojuego, serial):
        cursor = self.con.cursor()
        query = "insert into VideoJuego" \
                "(nombre, " \
                "release_date, " \
                "clasificacion, " \
                "consola, " \
                "empresa ," \
                "numero_jugadores, " \
                "tipo_juego," \
                "serial )  " \
                "values(" \
                " ?,?,?,?,?,?,?,?)"
        cursor.execute(query, (videojuego.nombre,
                               videojuego.release_date,
                               videojuego.clasificacion,
                               videojuego.consola,
                               videojuego.empresa,
                               videojuego.numero_jugadores,
                               videojuego.tipo_juego,
                               str(serial)))
        self.con.commit()

    def cargar_todo(self):
        from tienda_video_juegos.dominio.video_juego import VideoJuego

        cursor = self.con.cursor()
        video_juegos = cursor.execute(
            "select nombre,release_date,clasificacion,consola,"
            "empresa, numero_jugadores,tipo_juego,serial "
            " from videojuego")
        juegos = []
        for nombre, release_date, clasificacion, consola, empresa, \
            numero_jugadores, tipo_juego, serial in video_juegos:
            juego_cargado = VideoJuego(nombre, release_date, clasificacion,
                                       consola
                                       , empresa, numero_jugadores,
                                       tipo_juego, serial)
            juegos.append(juego_cargado)
        return juegos

    def cargar(self, id):
        from tienda_video_juegos.dominio.video_juego import VideoJuego

        cursor = self.con.cursor()
        video_juegos = cursor.execute(
            "select nombre,release_date,clasificacion,consola,"
            "empresa, numero_jugadores,tipo_juego,serial "
            " from videojuego where id = ?", (id,))
        juego_cargado = None
        for nombre, release_date, clasificacion, consola, empresa, \
            numero_jugadores, tipo_juego, serial in video_juegos:
            juego_cargado = VideoJuego(nombre, release_date, clasificacion,
                                       consola
                                       , empresa, numero_jugadores,
                                       tipo_juego, serial)
        return juego_cargado

    def actualizar(self, video_juego, id):
        print(id)
        query= 'update VideoJuego set nombre=?,release_date=?,clasificacion=?,'\
               'consola =?,empresa=?, numero_jugadores=?,tipo_juego=?,' \
               'serial=? '\
               'where id=?'
        cursor = self.con.cursor()
        cursor.execute(query,(video_juego.nombre,
                                video_juego.release_date,
                                video_juego.clasificacion,
                                video_juego.consola,
                                video_juego.empresa,
                                video_juego.numero_jugadores,
                                video_juego.tipo_juego,
                                video_juego.serial,
                                id))
        self.con.commit()
