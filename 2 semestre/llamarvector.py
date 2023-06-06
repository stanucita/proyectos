tamaño= int(input("ingrese el tamaño que desa del vector: "))
lista=[]

def llenarvector_ (lista,tamaño):
    for i in range (0,tamaño):
        numeros= input("ingresa la cantidad de numeros que desea mostrar: ")
        lista.append(numeros)
        print (lista)


print(llenarvector_(lista, tamaño))
