with open ("C:/Users/Camilo/Desktop/reportes/reporte2.txt", "r") as archivo:
    for linea in archivo.readlines():
        print("Esta es la cantidad de caracteres por linea", len(linea))
        print(linea, end="")