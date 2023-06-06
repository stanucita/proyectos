entrada= [int(x) for x in list(input().split())]

baldosas=[int(x) for x in list(input().split())]

fallas_totales = 0
fallas_sensor = 0
diccionario= dict()

for i in range(len(baldosas)):
    if (baldosas[i] in diccionario):
        fallas_totales += 1
    if  (baldosas[i] in diccionario and i - diccionario.get(baldosas[i]) <= entrada[1]):
        fallas_sensor += 1
    diccionario[baldosas[i]]= i

print (fallas_totales, fallas_sensor, entrada[0])