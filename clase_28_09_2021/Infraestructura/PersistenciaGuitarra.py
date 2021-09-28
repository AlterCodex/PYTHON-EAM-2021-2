import pickle
import sqlite3
import jsonpickle

from clase_28_09_2021.Dominio.guitarra import Guitarra


class PersistenciaGuitarra():

    def connect(self):
        self.con = sqlite3.connect("la_tienda_de_charly.sqlite")
        self.__crear_tabla()


    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE GUITARRA(serial text primary key, color text," \
                " modelo text, marca text,madera_del_mastil text," \
                " madera_del_diapason text, precio float, afinacion text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_guitarra(self,guitarra : Guitarra):
        cursor = self.con.cursor()
        query = "insert into GUITARRA(serial , color ," \
                " modelo , marca ,madera_del_mastil ," \
                " madera_del_diapason , precio , afinacion ) values(" \
                f" ?,?,?,?,?,?,?,{guitarra.afinacion})"
        cursor.execute(query,(str(guitarra.serial),guitarra.color,guitarra.modelo,
                              guitarra.marca,guitarra.madera_del_mastil,
                              guitarra.madera_del_diapason,guitarra.precio,guitarra.afinacion))
        self.con.commit()

    @classmethod
    def save(cls, guitarra):
        binary_open = open("files/"+str(guitarra.serial) + '.gui', mode='wb')
        pickle.dump(guitarra, binary_open)
        binary_open.close()


    @classmethod
    def load(cls, file_name):
        binary_open = open("files/"+file_name, mode='rb')
        guitarra = pickle.load(binary_open)
        binary_open.close()
        return guitarra


    @classmethod
    def save_json(cls, guitarra):
        text_open = open("files/"+str(guitarra.serial) + '.json', mode='w')
        json_gui = jsonpickle.encode(guitarra)
        text_open.write(json_gui)
        text_open.close()


    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/"+file_name, mode='r')
        json_gui = text_open.readline()
        guitarra = jsonpickle.decode(json_gui)
        text_open.close()
        return guitarra