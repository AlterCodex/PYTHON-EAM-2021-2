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
                    "serial text primary key, " \
                    "release_date text," \
                    "iva float, " \
                    "garantia int," \
                    "tipo text," \
                    "cantidad_disponible int," \
                    "prendido int) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass


    def guardar_producto(self, producto: Producto):
        cursor = self.con.cursor()
        query = "insert into Producto" \
                "(serial, " \
                "precio, " \
                "iva, " \
                "garantia, " \
                "tipo, " \
                "cantidad_disponible ," \
                "prendido )  " \
                "values(" \
                " ?,?,?,?,?,?,?)"
        cursor.execute(query, (str(producto.serial),
                               producto.precio,
                               producto.iva,
                               producto.garantia_meses,
                               producto.tipo,
                               producto.cantidad_disponible,
                               producto.prendido))
        self.con.commit()
        producto.articulo.guardar(producto.serial)
