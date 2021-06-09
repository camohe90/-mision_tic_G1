frases = []
contador = 1

with open("txt/reporte.txt", "r") as archivo:
    for linea in archivo.readlines():
        frases.append(linea.split())
    print(frases)


with open("txt/reporte_edit.txt", "w") as archivo:
    for frase in frases:
        
