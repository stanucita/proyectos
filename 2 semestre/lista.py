lista= []
adicion_lista= []
suma = 0

def lista_(lista):

    for i in range (10):
        numeros= input("ingresa al menos 10 numeros que desea sumar (numeros separados por un espacio): ")
        lista.append(numeros)
    print (lista)

def reverso_ (lista):
        for j in range (len(lista)-1,-1,-1):
            print ( lista[j])


print(lista_(lista))
print(reverso_(lista))