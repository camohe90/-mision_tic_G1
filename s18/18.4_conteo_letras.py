frase = input("Digite la frase que desea que verifiquemos")

conteo = {}

for letra in frase.lower():
    if letra not in conteo:
        conteo[letra] = 1
    else:
        conteo[letra] +=1

mensaje = (
    f"En la frase {frase} se encontraron las siguientes letras \n")
print(mensaje)
for clave, valor in conteo.items():
    print(f"letra {clave}: {valor}")
