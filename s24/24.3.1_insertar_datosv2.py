import sqlite3

datos = (4, "Hally", 2500)
print(type(datos))

conexion = sqlite3.connect("db/base_datos1.db")
print("Conexión exitosa")

cursor = conexion.cursor()

cursor.execute("INSERT INTO empleados (id, nombre, salario) VALUES(?,?,?)", datos)


conexion.commit()

