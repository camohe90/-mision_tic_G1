
frase = "Bienvenidos a una nueva sesion del curso de python 3"
frase2 = "Camilo"

print(type(frase))
print(len(frase))
print(len(frase2))

print(frase.upper())
print(frase.lower())

print(frase.replace("3","1"))

print(frase.title())

palabras = frase.split()
print(palabras)

print("-".join(palabras))

for palabra in palabras:
    print(palabra.capitalize(),end=" ")

