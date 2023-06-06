def write_messages():
    messages = []

    while True:
        # Pedimos al usuario que escriba un mensaje
        message = input("Escribe tu mensaje: ")
        date = input("Escribe la fecha (yyyy-mm-dd): ")
        time = input("Escribe la hora (hh:mm:ss): ")
        name = input("¿Quién escribe el mensaje?: ")

        # Agregamos el mensaje, la fecha, la hora y el nombre de quien lo escribió a la lista de mensajes
        messages.append(f"{date} {time} - {name}: {message}")

        # Preguntamos al usuario si desea seguir escribiendo mensajes
        continue_writing = input("¿Deseas escribir otro mensaje? (S/N): ")
        if continue_writing.lower() == "n":
            break

    # Imprimimos los mensajes en orden
    print("\nMensajes escritos:")
    for message in messages:
        print(message)

# Ejecutamos la función para escribir los mensajes
write_messages()

