
archivo = open("txt/reporte.txt", "w")
archivo.write("Hola clase\n")
archivo.write("Se esta acabando nuestro curso :(  :( ")
archivo.write("Hola")
archivo.close()

with open("txt/reporte.txt", "w") as archivo:
    archivo.write("Les queda un maravilloso camino por recorrer\n")
    archivo.write("El jueves espero que lleguen todos bañaditos para la foto")
