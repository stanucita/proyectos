class Vehiculo:

    def __init__(self, nombre, color):
        self.__nombre= nombre
        self.__color= color

    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color

    def get_nombre(self):
        return self.__nombre

class Auto(Vehiculo):
    def __init__(self, nombre, color, modelo):
        super().__init__(nombre, color)
        self.__modelo= modelo

    def getDescripcion(self):
        return self.get_nombre() + self.__modelo + " de color " + self.get_color()

c= Auto("Ford Mustang","rojo","GT350")
print(c.getDescripcion())
print(c.get_nombre())