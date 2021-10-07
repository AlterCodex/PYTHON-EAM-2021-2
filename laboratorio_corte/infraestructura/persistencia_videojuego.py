import sqlite3



class PersistenciaVideoJuego():

    def connect(self):
        self.con = sqlite3.connect("la_tienda_de_los_nerds.sqlite")
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
