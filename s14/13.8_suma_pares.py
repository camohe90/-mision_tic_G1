numeros_guardados = []
suma = 0

numeros_almacenar = int(input("Digita la cantidad de numero que desea almacenar"))

# Validar que el usuario ingrese un numero mayor que cero, que respresenta la cantida de elementos que quiere
while numeros_almacenar <= 0:
    print("Digite un numero mayor que cero")
    numeros_almacenar = int(input("Digita la cantidad de numero que desea almacenar"))

#  Guardar en la lista numeros_guardados, los numero que es usuario ingrese por teclado
for contador in range(numeros_almacenar):
    numeros_guardados.append(int(input(f"Digite el numero {contador +1} que desea almacenar")))

#imprimo la lista  de los numeros almacenados
print(numeros_guardados)

# Recorrer la lista numeros_guardados y voy a sumar solo pares
for numero in numeros_guardados:
    if numero % 2 == 0:
        suma = suma + numero

print(f"La suma de los numero pares es: {suma}")