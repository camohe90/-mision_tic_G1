import sqlite3
from sqlite3.dbapi2 import Cursor

conexion = sqlite3.connect("db/base_datos1.db")
print("Conexión exitosa")

cursor = conexion.cursor()

cursor.execute("INSERT INTO empleados VALUES(2, 'Pilar Herrera', 1400)")
cursor.execute("INSERT INTO empleados VALUES(3, 'Bolt', 200)")

conexion.commit()

