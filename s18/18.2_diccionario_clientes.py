contador = 1

clientes = {
    1234: ["Camilo" , "Molano", "Bogota"],
    4567: ["Alejandro" , "Herrera", "Cali"],
    890 :  ["Daniel" , "Gomez", "Tunja"],
    4689 :  ["Pilar" , "Diaz", "Medellin"],
    9876 : ["Jairo" , "Gomez", "Armenia"]
}


print(clientes[1234])
print(clientes[1234][2])

"""Error no existe el key
print(clientes[9999])"""

if (clientes.get(1234)):
    print("Cliente encontrado, esta es la informacion")
else:
    print("Cliente no encontrado")

if (clientes.get(7777)):
    print("Cliente encontrado")
else:
    print("Cliente no encontrado")

cedulas = tuple(clientes.keys())
print(cedulas)

informacion = tuple(clientes.values())
print(informacion)

for cliente in clientes:
    print(cliente)


for cliente in clientes.values():
    for dato in cliente:
        print(dato, sep=" ", end=" ")
    print()

for clave, valor in clientes.items():
    print(f"Esta es la cedula del cliente {contador} {clave} y esta es su informacion {valor}")
    contador +=1

