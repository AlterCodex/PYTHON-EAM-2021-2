import pickle
import sqlite3
import jsonpickle

from tienda_video_juegos.dominio.producto import Producto
from tienda_video_juegos.infraestructura.config import Config


class PersistenciaProducto():

    def connect(self):
        self.con = sqlite3.connect("la_tienda_de_los_nerds.sqlite")
        self.__crear_tabla()

    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE " \
                    "Producto(" \
                    "serial text primary key, " \
                    "precio float," \
                    "iva float, " \
                    "garantia int," \
                    "tipo text," \
                    "cantidad_disponible int," \
                    "prendido int) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_producto(self, producto : Producto):
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



    @classmethod
    def save(cls,producto):
        config=Config.obtener_instancia()
        if config.usaBase :
            persistencia = cls()
            persistencia.guardar_producto(producto)
        else:
            cls.save_json(producto)


    @classmethod
    def save_json(cls, producto):
        text_open = open("files/"+str(producto.serial) + '.json', mode='w')
        json_gui = jsonpickle.encode(producto)
        text_open.write(json_gui)
        text_open.close()


    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_gui = text_open.readline()
        producto = jsonpickle.decode(json_gui)
        text_open.close()
        return producto