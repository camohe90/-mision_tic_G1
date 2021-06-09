
with open ("txt/agregando_data.txt","w") as file:
    cantidad_numeros = int(input("Por favor ingresa la cantidad de numeros que quieres guardar"))
    for numero in range(cantidad_numeros):
        dato = input("Digite el numero que desea guardar: ")
        file.write(dato+ ",")