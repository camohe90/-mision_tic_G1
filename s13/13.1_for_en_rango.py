print("Vamos a contar de 1 a 10")

for contador in range(1,11):
    print(contador)

print("Vamos a contar lo numero impares de 1-10")

for contador in range (1,101,2):
    print(contador)

for linea in range(20):
    print("-", end=(""))

print("Vamos a contar lo numero pares de 1-10")

for contador in range (2,11,2):
    print(contador)

print("Vamos a contar de 50 -0")

for contador in range(50,-1,-5):
    print(f"Este es el numero {contador}")
    print("Este es el numero", contador)