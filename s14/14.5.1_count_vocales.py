vocales = "aeiou"
resultado = []

frase = input("Por favor ingrese la frase que desea que verifiquemos: ")

for vocal in vocales:
    conteo_vocales = frase.count(vocal)
    mensaje = f"En la frase hay {conteo_vocales} letras {vocal}"
    resultado.append(mensaje)

print(resultado)