import sqlite3


conexion = sqlite3.connect("db/base_datos1.db")
print("Conexión exitosa")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM empleados")

""" data = cursor.fetchall()
for linea in data:
    print(linea) """

[print(linea) for linea in cursor.fetchall()]

