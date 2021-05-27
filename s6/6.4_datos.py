#enteros
num1 = 20
num2 = 10
num3 = -15
num4 = 532131231

print(num1)
print(type(num1))
print(num4)
print(type(num4))

numero_flotante = round(10 / 3, 2)
print(numero_flotante)
print(type(numero_flotante))
print(4e7)
print(type(4e7))
print(pow(4,7))

x = 2 + 3j
print(type(x))
print(x.real)
print(x.imag)

frase = "Esto es una cadena de texto" # Esto es un string
print(frase)
print(frase[0])
print(len(frase))

lista = [1,2,3,4,5,6,7,8,9,10] #son mutables 
print(lista[0])
print(lista[-1])
print(lista[0:4])

lista2 = ["hola", 1, 2.2 , [3,2]]
print(lista2[2])
print(lista2[3][0])


lista = []
lista.append(11)
print(lista)

tupla = (1,2,3,4, "numeros") #son inmutables
print(tupla)
print(tupla[-1])
#tupla[1]=3

set_datos = {5,2,4,5,6,21,3,4,5,1}
print(set_datos)

futbolistas = {
    1 : "Ospina", 
    13 : "Mina",
    10 : "James", 
    5 : "Puyol",
    9 : "Falcao", 
    19 : "Muriel",
    11: "Cuadrado", 
    18 : "Fabra",
    6: "Barrios",  
    3: "Murillo",
    'defensa1' : "Zapata"
}

print(futbolistas[1])
print(futbolistas['defensa1'])