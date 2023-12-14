# Iimporta el módulo MYSQL
import mysql.connector as  mysql

# Crea la conexión
def conectar():
    try:
        conexion = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database="libros"
            )
        print("Se ha conectado a la DB correctamente")
        return conexion
    except mysql.Error as err:
        print("(Ha ocurrido un error", err)
        
        
