
frases = []

with open("txt/reporte.txt", "r") as archivo:
    for linea in archivo.readlines():
        print(linea)
        frases.append(linea.split())

for linea in frases:
    for palabra in linea:
        print(palabra)