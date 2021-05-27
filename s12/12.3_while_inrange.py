numero = int(input("Ingrese un numero sea mayor que 0 y menor que 20: "))

while numero < 0 or numero >= 20:
    numero = int(input("Error -> Por favor ingrese un numero sea mayor que 0 y menor que 20: "))

print(numero)