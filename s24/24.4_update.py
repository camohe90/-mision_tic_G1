import sqlite3


conexion = sqlite3.connect("db/base_datos1.db")
print("Conexión exitosa")

cursor = conexion.cursor()

cursor.execute("UPDATE empleados SET nombre = 'Camilo Molano Herrera' where id = 1")


conexion.commit()

