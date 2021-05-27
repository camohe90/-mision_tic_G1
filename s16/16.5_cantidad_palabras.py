def contar_palabras(frase = "falta123"):
    """Esta funcion retorna la cantidad de palabras de un string

        Parametros:
        frase: string

        Return:
        numero: int cantidad de palabras
    """
    if frase == "falta123":
        return "Por favor revise la frase que envio"
    else:
        lista_mensaje = frase.split()
        return len(lista_mensaje)

print(contar_palabras.__doc__)


frase_inicial = input("Digite la frase que desa verificar: ")
print(f"La frase tiene {contar_palabras(frase_inicial)}")

print(f"La frase tiene {contar_palabras()}")