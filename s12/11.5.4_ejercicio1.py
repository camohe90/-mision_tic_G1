"""Determinar la cantidad de dinero que recibirá un trabajador por
concepto de las horas extras trabajadas en una empresa, sabiendo
que cuando las horas de trabajo exceden de 40, el resto se
consideran horas extras y que estas se pagan al doble de una hora
normal cuando no exceden de 8; si las horas extras exceden de 8 se
pagan las primeras 8 al doble de lo que se pagan las horas normales
y el resto al triple"""

VALOR_HORA = 10000
horas_trabajadas_mes = int(input("Por favor ingrese la cantidad de horas trabajadas: "))


if (horas_trabajadas_mes<=40):
    salario = horas_trabajadas_mes*10000
    print(f"El salario del mes es: {salario}")
elif (horas_trabajadas_mes>40 and  horas_trabajadas_mes<=48):
    horas_recargo = horas_trabajadas_mes - 40
    salario = (horas_trabajadas_mes -  horas_recargo) * VALOR_HORA + (horas_recargo * (VALOR_HORA*2))
    print(f"El salario del mes es: {salario}")
elif(horas_trabajadas_mes > 48):
    horas_recargo= horas_trabajadas_mes - 40
    horas_triples = horas_recargo - 8
    horas_dobles = 8
    salario = (horas_trabajadas_mes -  horas_recargo) * VALOR_HORA + (horas_recargo * (VALOR_HORA*2))



 