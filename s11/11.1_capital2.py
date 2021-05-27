INTERES_ANUAL = 0.15
INTERES_MENSUAL = INTERES_ANUAL / 12

capital = float(input("Por favor ingrese el capital que sea invertir: "))
numero_meses = int(input("Por favor ingrese el número de meses que desea invertir el dinero: "))

rendimiento = (capital * numero_meses * INTERES_MENSUAL)

print(rendimiento)

print(f"Su nuevo saldo despues de {numero_meses} es {capital+rendimiento}")