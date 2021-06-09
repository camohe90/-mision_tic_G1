import sqlite3


conexion = sqlite3.connect("db/base_datos1.db")
print("Conexión exitosa")

cursor = conexion.cursor()

cursor.execute("DELETE from empleados where id =1 ")
#cursor.execute("DELETE from empleados where id between 2 and 3")


conexion.commit()
