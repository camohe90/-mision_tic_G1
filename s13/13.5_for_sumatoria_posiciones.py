suma = 0
suma2 = 0
numeros_usuario = [1,2,3,4,5,6,7,8,9,10]

for numero in range(0, len(numeros_usuario),2):
    print(numeros_usuario[numero])
    suma = suma + numeros_usuario[numero]

print("La suma de los elementos en la posiciones pares del arreglo es: ", suma)


for numero in range(1, len(numeros_usuario),2):
    print(numeros_usuario[numero])
    suma2 = suma2 + numeros_usuario[numero]

print("La suma de los elementos en la posiciones impares del arreglo es: ", suma2)