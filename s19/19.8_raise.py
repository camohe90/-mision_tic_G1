numero = int(input("Ingrese un numero"))

try:
    if numero < 10:
        raise ValueError("ERROR-> 1231232")
except ValueError as error:
    print("Vamos a ver el error")
    print(error.args[0])