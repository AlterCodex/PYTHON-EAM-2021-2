

class Guitarra:


    def __init__(self, color, modelo, marca,
                 madera_del_mastil='Roble', madera_del_diapason='Roble', precio=0,
                 afinacion='RE',  *args, **kargs):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.serial = '123465789'
        self.afinacion = afinacion
        self.madera_del_mastil = madera_del_mastil
        self.madera_del_diapason = madera_del_diapason
        self.precio =precio


    def __str__(self):
        return  f"{self.serial}--{self.color}--{self.marca}--{self.modelo}"

    def __repr__(self):
        return 'Soy una guitarra'

    def pintar(self, nuevo_color):
        self.color = nuevo_color


    def apreciar(self, nuevo_precio):
        self.precio = nuevo_precio

    def buscar(self, marca):
        return None
