def valor_absoluto(numero_validar):
    """ Esta funcion retorna el valor absoluto

        parametros:
        numero_validar: float

        return:
        numero: flotante con el valor absoluto
    """
    if numero_validar > 0:
        return numero_validar
    else:
        return -numero_validar

# Para imprimir la documentación de la funcion puedo utlizar
# print(valor_absoluto.__doc__)

numero = float(input("Digite el numero que desea obtener el valor absoluto: "))
print(f"El valor absoluto de {numero} es {valor_absoluto(numero)}" )


def sumar(numero_1, numero_2):
    resultado_suma = numero_1 +  numero_2
    return resultado_suma

def multiplicar(numero1, numero2):
    resultado_multiplicacion =  numero1 * numero2
    return resultado_multiplicacion