lista_= []
def conteo (lista_):
    valores= input().split()
    lista_.append(valores)

    print (lista_)

def pregunta_(lista_):
    pregunta1= input("¿desea borar algun valor de la lista? (recuerde que la lista funciona desde la posicion 0): ")
    
    if pregunta1 == 'si':
        preguntaborrado= int(input("¿que posicion de la lista desea borrar? "))
        lista_.remove(preguntaborrado)
    elif pregunta1 == 'no':
        print("Ok.")



print(conteo(lista_))
print(pregunta_(lista_))
    
