filas = int(input("filas: "))
caracter = input("caracter: ")

if filas <= 0 or not caracter:
    print("Error")

elif caracter == " ":
    print("Error")
else:
    for i in range(filas):
        for j in range(filas-i-1):
            print(" ", end=" ")
        for j in range(2*i+1):
            print(caracter, end=" ")
        print()
    for i in range(filas-2, -1, -1):
        for j in range(filas-i-1):
            print(" ", end=" ")
        for j in range(2*i+1):
            print(caracter, end=" ")
        print()






