factorial_n = 1
factorial_m = 1
factorial_nm = 1

numero_n = int(input("Digite un numero n: "))
numero_m = int(input("Digite un numero m: "))

while numero_n < numero_m:
    print("Por favor verifica que el numero n sea mayot que m")
    numero_n = int(input("Digite un numero n: "))
    numero_m = int(input("Digite un numero m: "))

numero_n_m = numero_n - numero_m

for numero in range(1, numero_n +1):
    factorial_n = factorial_n * numero

for numero in range(1, numero_m +1):
    factorial_m = factorial_m * numero

for numero in range(1, numero_n_m +1):
    factorial_nm = factorial_nm * numero


combinatoria = factorial_n / (factorial_nm * factorial_m) 

print(f"La combinatoria de {numero_n} y {numero_m} es igual a {combinatoria}")
