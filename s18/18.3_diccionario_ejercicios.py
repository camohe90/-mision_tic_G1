from os import system
system("cls")


consultar = True

agenda_telefonos = {
    "Camilo" : 12345,
    "Alejandro" : 4567,
    "Daniel": 89012,
    "Pilar" : 5678,
    "Jairo" : 76543
}

mensaje = (
    f"---------------------------------------------------------------\n"
    f"Bienvenidos a la agenda de telefonos python mision tic\n"
    f"---------------------------------------------------------------\n"
    f"Usted cuenta con las siguientes opciones \n"
    f"1. Consultar Contacto\n"
    f"2. Añadir Contacto\n"
    f"3. Modificar Contacto\n"
    f"4. Borrar Contacto\n"
    f"5. Salir\n"
)

while consultar:
    print(mensaje)
    opcion = input("Por favor elija una de las opciones definidas")

    while opcion not in ("1","2","3","4","5"):
        opcion = input("Por favor elija una opcion valida")
    
    if opcion == "1":
        nombre = input("Por favor digite el nombre que desea consultar: ")
        if nombre not in agenda_telefonos:
            print("--------------------------------------")
            print("El nombre ingresado no se encuentra en su agenda")
        else:
            telefono = agenda_telefonos[nombre]
            print("--------------------------------------")
            print(f"Encontramos la siguiente informacion en su agenda\n{nombre} : {telefono}")
    if opcion == "2":
        nombre = input("Por favor digite el nombre que desea añadir: ")
        if nombre in agenda_telefonos:
            print("--------------------------------------")
            print("El nombre ya se encuentra su agenda")
        else: 
            telefono = int(input("Por favor ingrese el numero de telefono: "))
            agenda_telefonos[nombre] = telefono
            print("--------------------------------------")
            print("El contacto se ha guardado correctamente")
    if opcion == "3":
        nombre = input("Por favor digite el nombre que desea modificar: ")
        if nombre not in agenda_telefonos:
            print("--------------------------------------")
            print("El nombre ingresado no se encuentra en su agenda")
        else:
            telefono = int(input("Por favor ingrese el nuevo numero de telefono: "))
            agenda_telefonos[nombre] = telefono
            print("--------------------------------------")
            print(f"El telefono ha sido modificiado correctamente")
    if opcion == "4":
        nombre = input("Por favor digite el nombre que desea borrar: ")
        if nombre not in agenda_telefonos:
            print("--------------------------------------")
            print("El nombre ingresado no se encuentra en su agenda")
        else:
            del agenda_telefonos[nombre]
            print("--------------------------------------")
            print("El telefono ha sido eliminado correctamente")
    if opcion == "5":
        consultar = False

print("Programa finalizado")