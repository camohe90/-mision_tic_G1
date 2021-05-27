
numero1 = int(input("Por favor ingrese el numero 1:"))
numero2 = int(input("Por favor ingrese el numero 2:"))

if numero1 == numero2:
    resultado = numero1 * numero2
    print(f"El resultado es: {resultado}")
else:
    if numero1 > 5 and numero1 <=10:
        resultado = numero1 + numero2
        print(f"El resultado es: {resultado}")
    else: 
        resultado = numero1 - numero2
        print(f"El resultado es: {resultado}")