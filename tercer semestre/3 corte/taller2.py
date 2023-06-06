"""
Nombre:Daniel Patarroyo Laverde
Fecha:18/04/23
Descripción: Implementación básica de una Cola mediante una Lista Enlazada
"""

# Definición de la clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Definición de la clase Cola
class Cola:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def is_empty(self):
        if self.cabeza is None:
            return True
        else:
            return False
    def enqueue(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cola is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            nodo_eliminar = self.cabeza
            self.cabeza = nodo_eliminar.siguiente
            if self.cabeza is None:
                self.cola = None
            return nodo_eliminar.dato
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.cabeza.dato

# Definición de la función principal main()
def main():
    mi_cola = Cola()
    mi_cola.enqueue(1)
    mi_cola.enqueue(2)
    mi_cola.enqueue(3)
    mi_cola.enqueue(4)
    
    print("Cola inicial:")
    while not mi_cola.is_empty():
        print(mi_cola.dequeue())
    
    mi_cola.enqueue(5)
    mi_cola.enqueue(6)
    
    print("Cola luego de eliminar elementos:")
    while not mi_cola.is_empty():
        print(mi_cola.dequeue())





 

main() # Llamado a la función principal main()