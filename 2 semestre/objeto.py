


class Poligono:
    """define un poligono segun su base y su altura."""

    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return self.b * self.h

class Rectangulo(Poligono):
    def area(self):
        return self.b * self.h

class Triangulo(Poligono):

    def area(self):
        return (self.b * self.h) / 2

rectangulo =Rectangulo(20, 10)
triangulo = Triangulo(20, 12)

#def menu():
#    for i in ():
#        pregunta= input("Hola, ¿a cual figura deseas conocer su area rectangulo, triangulo, poligono? ")
#        if pregunta == 'rectangulo':
#            print("El area del rectangulo es:", Rectangulo.area())
#        elif pregunta == 'triangulo':
#            print("el area del tringulo es: ", Triangulo.area())
#        elif pregunta == 'poligono':
#            print("el area del poligono es:", Poligono.area())
#        else:
#            print ('error')
        

#print(menu())