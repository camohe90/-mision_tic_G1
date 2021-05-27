MAYORIA_EDAD = 18

edad = int(input("Ingresa tu edad"))

if edad >= MAYORIA_EDAD:
    print("Puedes ingresar al bar")
else:
    print("No puedes ingregar al bar")
    edad_restante = MAYORIA_EDAD - edad
    print("Puedes intentar ingresar en", edad_restante, "años")