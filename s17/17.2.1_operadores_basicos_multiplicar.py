numeros1 = [1,2,3,4,5]
numeros2 = [1,2,3,4,5]
resultado = [] 
resultado2 = []

for elemento in range(len(numeros1)):
    suma_listas = numeros1[elemento] + numeros2[elemento]
    resultado.append(suma_listas)
print(resultado)

for elemento in range(len(numeros1)):
    suma_listas = numeros1[elemento] + numeros2[len(numeros1)-1-elemento]
    resultado2.append(suma_listas)
print(resultado2)