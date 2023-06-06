historial = []

while True:
    opcion = input("¿Quieres agregar una nueva entrada al historial? (si/no): ")
    if opcion == "no":
        break
    
    nombre = input("Ingrese el nombre de la persona: ")
    duracion = input("Ingrese la duración de la llamada (en minutos): ")
    contesto = input("¿Contestó la llamada? (si/no): ")
    
    if contesto == "si":
        historial.append({"nombre": nombre, "duracion": duracion, "contestada": True})
    else:
        historial.append({"nombre": nombre, "duracion": "N/A", "contestada": False})

print("\nHistorial de llamadas:")
for llamada in historial:
    if llamada["contestada"]:
        print(f"Llamada con {llamada['nombre']} duró {llamada['duracion']} minutos.")
    else:
        print(f"Llamada perdida de {llamada['nombre']}.")
