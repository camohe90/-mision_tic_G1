agenda_telefonos = {
    "Camilo" : 12345,
    "Alejandro" : 4567,
    "Daniel": 89012,
    "Pilar" : 5678,
    "Jairo" : 76543
}

print(agenda_telefonos)

print(agenda_telefonos["Camilo"])
print(agenda_telefonos["Jairo"])
nuevo_telefono = 3016252610
agenda_telefonos["Camilo"] = nuevo_telefono
print(agenda_telefonos["Camilo"])

agenda_telefonos.pop("Daniel")
print(agenda_telefonos)

""" del agenda_telefonos["Daniel"]
print(agenda_telefonos) """

agenda_telefonos["Nombre2"] = 5555
print(agenda_telefonos)

