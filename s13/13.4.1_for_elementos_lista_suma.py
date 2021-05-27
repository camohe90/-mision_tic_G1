suma = 0
suma2 = 0
numeros_usuario = [1,2,3,4,5,6,7,8,9,10]

#print(sum(numeros_usuario))

for numero in numeros_usuario:
    suma = suma + numero

print("La suma es del primer for es", suma)

print(len(numeros_usuario))

for elemento in range(len(numeros_usuario)):
    suma2 = suma2 + numeros_usuario[elemento]

print("La suma es del segundo for es", suma2)