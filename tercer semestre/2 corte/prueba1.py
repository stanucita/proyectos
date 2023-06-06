'''
Nombre: Daniel Patarroyo Laverde - Johan Sebastian Quintero
Fecha: 9/03/2023
Descripción: solicitar al usuario un maximo de 100 uno a uno y guardarlos en un vector lista. luego inicialice dos vectores  con el fin de que uno 
contenga los elementos diferentes que ay con respecto a los del valor inicial y el otro con la cantidad de veces  que un determinado caracter  aparece en el 
vetor inicial solo se debera escribir cuantos y cuales  elementos diferentes se encontraron y la cantidad de veces  usando nada mas que la funcion predeterminada 
len  
'''
# Solicitamos los números al usuario
numeros = []
while True:
    numero = input("Ingrese un número (o presione Enter para terminar): ")
    if numero == "":
        break
    numero = int(numero)
    if numero > 0 and len(numeros) < 100:
        numeros.append(numero)
    elif numero <= 0:
        print("Error: El número debe ser mayor que cero.")
    else:
        print("Error: No se pueden ingresar más de 100 números.")
        break

elementos_diferentes = list(set(numeros))
cantidades = [numeros.count(elemento) for elemento in elementos_diferentes]

print("Elementos diferentes encontrados:", len(elementos_diferentes))
print("Cantidad de veces que aparece cada elemento:")
for i in range(len(elementos_diferentes)):
    print(f"{elementos_diferentes[i]}: {cantidades[i]}")

