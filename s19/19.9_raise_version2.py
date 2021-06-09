direcciones = [3,4,5,6,7,8]

def agregar_datos(lista, elemento):
    if elemento in lista:
        raise ValueError(f"ERROR -> No se pueden añadir elementos duplicados {elemento}", "ERROR3433")
    lista.append(elemento)

try:
    agregar_datos(direcciones, 10)
    agregar_datos(direcciones, 3)
except ValueError as error:
    print(error.args)
else:
    print("Elementos agregados correctamente")
finally:
    print(f"La lista resultante es {direcciones}")