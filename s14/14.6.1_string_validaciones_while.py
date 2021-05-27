palabra = input("Digite la palabra para continuar")

while not (palabra.isalpha()):
    palabra = input("Digite la palabra para continuar")

print(palabra)