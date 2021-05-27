""" Realizar un codigo que simule una persona que saluda a otra, solicitar que el usuario ingrese su comida  favorita y su color favorito. El sistema debe imprimir un unico mensaje saludando como el ejemplo y diciendo algun mensaje referente a la comida y al color"""

print("Manejo de información de entrata con python")
print("--------------------------------------------------")
primer_nombre = input("Por favor ingrese su nombre: ")  #Guardo la información ingresada por teclado  en la variables primer_nombre
primer_apellido = input("Por favor ingrese su apellido: ") #Guardo la información ingresada por teclado  en la variables primer_apellido
comida = input("Por favor ingrese tu comida favorita: ")
color = input("Por favor ingrese tu color favorito: ")

print("Hola", primer_nombre,primer_apellido,"es un gusto saludarte")
print("A mi tambien me gusta la", comida ,"pero mi color favorito no es el", color , "es el verde")

print(type(primer_nombre))
print(type(primer_apellido))
print(type(comida))
print(type(color))

