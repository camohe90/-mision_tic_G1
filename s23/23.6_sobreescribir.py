contador = 1

palabras = ["hola", "como", "estan", "ya", "casi", "son", "expertos", "en", "python"]

with open ("txt/reporte3.txt", "w") as archivo:
    for palabra in palabras:
        archivo.write( str(contador) + palabra + "\n")
        contador+=1

