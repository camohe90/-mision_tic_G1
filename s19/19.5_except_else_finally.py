"""La sentencia try tiene otra cláusula opcional cuyo objetivo es definir las acciones de limpieza que deben
ejecutarse en cualquier circunstancia.
• Una cláusula finally se ejecuta antes de salir de la sentencia try, tanto si se ha producido una excepción
como si no. 

Cuando se ha producido una excepción en la cláusula try y no ha sido manejada por una
cláusula except, se vuelve a lanzar después de que se haya ejecutado la cláusula finally.

La cláusula finally también se ejecuta "a la salida" cuando se sale de cualquier otra cláusula de la sentencia try utilizando break/continue/return"""



try:
    resultado = 14 + "30"
except TypeError:
    print("ERROR -> Intento de suma de numero y cadena")
else:
    print("Operacion realizada correctamente")
finally:
    print("Sea lo que sea yo me voy a ejecutar y soy el cierre del try")


try:
    resultado = 14/0 
except TypeError:
    print("ERROR -> Intento de suma de numero y cadena")
except:
    print("Hay otro tipo de error")
else:
    print("Operacion realizada correctamente")
finally:
    print("Sea lo que sea yo me voy a ejecutar y soy el cierre del try")