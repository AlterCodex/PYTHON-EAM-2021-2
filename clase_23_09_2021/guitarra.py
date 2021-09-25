import uuid
import pickle
import jsonpickle
class Guitarra:


    def __init__(self, color, modelo, marca,
                 madera_del_mastil='Roble', madera_del_diapason='Roble', precio=0,
                 afinacion='RE',  *args, **kargs):
        self.color= color
        self.marca = marca
        self.modelo = modelo
        self.serial = uuid.uuid4()
        self.afinacion = afinacion
        self.madera_del_mastil = madera_del_mastil
        self.madera_del_diapason = madera_del_diapason
        self.precio =precio


    def __str__(self):
        return  f"{self.serial}--{self.color}--{self.marca}--{self.modelo}"

    def __repr__(self):
        return str(self.serial)
    def pintar(self, nuevo_color):
        self.color = nuevo_color


    def apreciar(self, nuevo_precio):
        self.precio = nuevo_precio

    def cumple(self, especificacion):
        dict_guitarra = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_guitarra or dict_guitarra[k] != especificacion.get_value(k):
                return False
        return  True

    @classmethod
    def save(cls, guitarra):
        binary_open= open(str(guitarra.serial)+'.gui', mode='wb')
        pickle.dump(guitarra,binary_open)
        binary_open.close()

    @classmethod
    def load(cls, file_name):
        binary_open = open(file_name, mode='rb')
        guitarra=pickle.load(binary_open)
        binary_open.close()
        return guitarra

    @classmethod
    def save_json(cls, guitarra):
        text_open= open(str(guitarra.serial)+'.json', mode='w')
        json_gui=jsonpickle.encode(guitarra)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open(file_name, mode='r')
        json_gui=text_open.readline()
        guitarra=jsonpickle.decode(json_gui)
        text_open.close()
        return guitarra