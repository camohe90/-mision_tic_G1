"""Programa que me permita ingresar 10 numeros
    me imprima el promedio de los numeros ingresados
    me imprima el mayor y el menor
    que me genere una lista con los pares y otra con los impares"""

numeros_ingresados= []
pares = []
impares  = []
total = 0

for numero in range(10):
    mensaje = f"ingrese el numero {numero+1}:"
    numero_ingresado = int(input(mensaje))
    numeros_ingresados.append(numero_ingresado)

for numero in numeros_ingresados:
    total += numero
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

promedio = total / len(numeros_ingresados)
menor = min(numeros_ingresados)
mayor = max(numeros_ingresados)

print(f"El promedio de los numeros ingresados es: {promedio}")
print(f"El numero menor en la lista de numeros ingresados es: {menor}")
print(f"El numero mayor en la lista de numeros ingresados es: {mayor}")
print(f"Los numero pares que hay en la lista son {pares}")
print(f"Los numero impares que hay en la lista son {impares}")







