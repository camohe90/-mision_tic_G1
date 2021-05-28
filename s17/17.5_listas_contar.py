repeticion = []

numeros = input("Digite las notas que desea registrar separadas por comas")

notas = numeros.split(",")

print(notas)
notas_filtradas = set(notas)
print(notas_filtradas)

for nota in sorted(notas_filtradas):
    repeticion.append(f"La {nota} se repite {notas.count(nota)} veces")

print(repeticion)