"""
Nombre:Daniel Patarroyo Laverde 
Fecha:13-04.2023
Descripción: Implementación básica de una Pila mediante una Lista Enlazada
"""

# Definición de la clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
 
# Definición de la clase Pila
class Pila:
    def __init__(self):
        self.cabeza = None

    def is_empty(self):
        if self.cabeza == None:
            return True
        else:
            return False

    def push(self, dato):
        if self.is_empty():
            self.cabeza = Nodo(dato)
        else:
            nuevo_nodo = Nodo(dato)
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    def pop(self):
        if self.is_empty():
            return None
        else:
            nodo_eliminar = self.cabeza
            self.cabeza = self.cabeza.siguiente
            nodo_eliminar.siguiente = None
            return nodo_eliminar.dato
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.cabeza.dato



# Definición de la función principal main()


def main():
    mi_pila = Pila()
    mi_pila.push(1)
    mi_pila.push(2)
    mi_pila.push(3)
    mi_pila.push(4)

    print("Pila inicial:")
    while not mi_pila.is_empty():
        print(mi_pila.pop())

    mi_pila.push(1)
    mi_pila.push(2)

    print("Pila luego de eliminar 2 elementos:")
    while not mi_pila.is_empty():
        print(mi_pila.pop())



main()
 # Llamado a la función principal main(),