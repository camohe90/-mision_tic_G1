"""Un vendedor recibe un sueldo base, mas un 10% extra por comisión de
sus ventas, el vendedor desea saber cuanto dinero obtendrá por
concepto de comisiones por las tres ventas que realiza en el mes y el
total que recibirá en el mes tomando en cuenta su sueldo base y
comisiones."""

# Variables que me da el ejercicio
PORCENTAJE_COMISION = 0.10

# Información de entrada
salario_base = float(input("Ingrese su sueldo base: "))

# Proceso
comision = salario_base * PORCENTAJE_COMISION

# Salida
print("Su comisión este mes es de", comision)
print("El salario total que recebiria este mes es:", (salario_base + comision))
