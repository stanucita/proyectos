import time

# Función para mostrar el círculo de carga
def mostrar_circulo_de_carga(segundos):
    for i in range(segundos):
        # Cada iteración muestra el siguiente carácter del círculo de carga
        print("Cargando" + "." * i)
        # Espera un segundo antes de mostrar el siguiente carácter
        time.sleep(1)
    # Después de 15 segundos, muestra el mensaje de última actualización
    print("Última actualización: 20/03/2023-02:15:00")

# Llama a la función para mostrar el círculo de carga durante 15 segundos
mostrar_circulo_de_carga(15)