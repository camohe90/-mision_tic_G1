lineas_archivo = []
contador = 1


with open ("C:/Users/Camilo/Desktop/reportes/reporte2.txt", "r") as archivo:
    for linea in archivo.readlines():
        lineas_archivo.append(linea)

print(lineas_archivo)
print("El archivo tiene", len(lineas_archivo), "lineas")

for linea in lineas_archivo:
    print(f"En la linea {contador} esta esta informacion: {linea}", end="")
    print(linea[:4])
    contador+=1

