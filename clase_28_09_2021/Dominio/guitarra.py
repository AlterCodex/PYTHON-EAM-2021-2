import uuid
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

