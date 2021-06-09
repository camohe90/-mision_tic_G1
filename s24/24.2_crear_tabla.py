import sqlite3

conexion = sqlite3.connect("db/base_datos1.db")
print("Conectado exitosamente")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE empleados(id integer PRIMARY KEY, nombre text, salario real)")

conexion.commit() # Guardo todos los cambios que hicimos