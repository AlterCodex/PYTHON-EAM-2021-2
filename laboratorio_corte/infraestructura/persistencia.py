import pickle
import sqlite3
import jsonpickle

from laboratorio_corte.dominio.producto import Producto


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