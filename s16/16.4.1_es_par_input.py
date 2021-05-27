numero_revisar = 0

def  es_par(numero):
    if numero % 2 == 0:
        return "Es par"
    else:
        return "No es par"


while numero_revisar != -1 :
    numero_revisar = int(input("Por favor digite el numero que desea validar: "))
    print("El numero", numero_revisar,  "es", es_par(numero_revisar))