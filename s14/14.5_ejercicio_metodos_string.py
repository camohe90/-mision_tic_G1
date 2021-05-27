nombre = input("Introduzca su nombre completo: ")

lista_nombre = nombre.split()
print(lista_nombre)

union = "".join(lista_nombre)
print(union)
union = "**".join(lista_nombre)
print(union)
cantidad_letras = len(union)

print(f"La cantidad de letras que tiene su nombre es {cantidad_letras}")