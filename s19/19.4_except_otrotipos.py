from sys import exc_info

try:
    numero = int(input("Digite un numero"))
    print("El resultado del la division es", 1/numero)

except(ValueError, TypeError, IndexError):
    print("Tiene un erorr al introducir los datos: ")
    error = exc_info()
    print(type(error))
    print("El error es", error[0])

except ZeroDivisionError:
    print("Hay una division entre cero")
    error = exc_info()
    print(type(error))
    print("El error es", error[0])
    
except:
    print("Ocurrio un error")