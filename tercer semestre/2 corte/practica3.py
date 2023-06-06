from tqdm import tqdm
import time

a= int(input("Ingrese numero de telefono: "))

items = list(range(0, 100))

for item in tqdm(items):
    time.sleep(0.1)

print("Cifrado de extremo a extremo activo con el número: {}".format(a))

print("end-to-end encryption only allows data information to be stored on the device of use.")