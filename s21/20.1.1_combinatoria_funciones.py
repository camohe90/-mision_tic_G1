from funciones import combinatoria

numero_n = int(input("Digite un numero n: "))
numero_m = int(input("Digite un numero m: "))

while numero_n < numero_m:
    print("Por favor verifica que el numero n sea mayot que m")
    numero_n = int(input("Digite un numero n: "))
    numero_m = int(input("Digite un numero m: "))

resultado_combinatoria = combinatoria(numero_n, numero_m)

print("El resultado de la combinatoria es", resultado_combinatoria)



