import time

# Duración de la descarga en segundos
duracion_descarga = 8 * 60 * 60

# Velocidad de descarga en bytes por segundo
velocidad_descarga = 1000

# Tamaño total del archivo en bytes
tamanio_archivo = 10000000

# Tiempo de inicio de la descarga
inicio_descarga = time.time()

# Inicializar el progreso de la descarga en 0%
progreso_descarga = 0

while time.time() - inicio_descarga < duracion_descarga:
    # Calcular el progreso actual de la descarga
    progreso_descarga = (time.time() - inicio_descarga) / duracion_descarga
    
    # Calcular la cantidad de bytes descargados hasta el momento
    bytes_descargados = int(tamanio_archivo * progreso_descarga)
    
    # Calcular el tiempo restante de la descarga
    tiempo_restante = int((tamanio_archivo - bytes_descargados) / velocidad_descarga)
    
    # Imprimir el progreso de la descarga
    print("Progreso: {:.2%} - Descargados: {} bytes - Tiempo restante: {} segundos".format(
        progreso_descarga, bytes_descargados, tiempo_restante))
    
    # Esperar un segundo antes de volver a comprobar el progreso
    time.sleep(1)