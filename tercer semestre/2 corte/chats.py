fecha = "23-03-2023"
horas = input("Ingrese las horas separadas por comas (formato HH:MM): ").split(",")
nombres = []

while True:
    nombre = input("Ingrese un nombre (o presione 'q' para salir): ")
    if nombre == "q":
        break
    nombres.append(nombre)

for hora in horas:
    print(fecha + " " + hora)
    for nombre in nombres:
        print(nombre + " - " + fecha + " " + hora)
