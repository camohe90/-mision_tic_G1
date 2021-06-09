from tkinter import StringVar


def factorial(limite):
    resultado = 1
    for numero in range(1, limite+1):
        # resultado = resultado * numero
        resultado*= numero
    return resultado

def combinatoria(numero1, numero2):
    resultado = factorial(numero1) / (factorial(numero1 - numero2) * factorial(numero2)) 
    return resultado

def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

