import sqlite3


conexion = sqlite3.connect("db/base_datos1.db")
print("Conexión exitosa")

cursor = conexion.cursor()

cursor.execute("SELECT id, nombre FROM empleados where salario >450 and salario < 1460")

[print(linea) for linea in cursor.fetchall()]

