frutas = ["Banano", "Coco", "Lulo", "Manzana" , "Pera"]
frutas2 = ("Banano", "Coco", "Lulo", "Manzana" , "Pera")

numeros = [10,5,6,2,4,6,7,100,25]
numeros2 = (10,5,6,2,4,6,7,100,25)

varios_elementos = ["hola" , [1,2,3], 10.5]

lista2 = [1,2]
print(type(lista2))
tupla = (2,2)
print(type(tupla))

print(frutas[0], frutas2[0])

print(numeros[2:6])
print(numeros2[2:6])

print(min(frutas), "," ,  min(frutas2))
print(max(frutas), "," ,  max(frutas2))

frutas.append("Piña")
print(frutas)

#frutas2.append("Piña")  No puedo agregar elementos a una tupla
#print(frutas2)
frutas.sort()
print(frutas)

#frutas2.sort()   No puedo modificar la  tupla original
#print(frutas2)

print(sorted(frutas))
print("Ya se ejecuto")
print(tuple(sorted(frutas2)))


#frutas_ordenadas = sorted(frutas)
#print(frutas_ordenadas)








