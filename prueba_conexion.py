import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host = 'db4free.net',
        port = 3306,
        user = 'ulises2',
        password = '1234567!',
        db = 'proyectodb'
    )

    if conexion.is_connected():
        print("Conexión exitosa")
        infoServer = conexion.get_server_info()
        print("Info del servidor: ",infoServer)
        cursor = conexion.cursor()
        cursor.execute("SELECT database()")
        registro = cursor.fetchone()
        print("Conectado a la base de datos ",registro)
        cursor.execute("SELECT * FROM tabla_prueba")
        resultados = cursor.fetchall()
        for fila in resultados:
            print("Número de estudiante: ",fila[0])
            print("Nombre del estudiante: ",fila[1])
            print("Edad del estudiante: ",fila[2])
            print("Carrera: ",fila[3])

except Error as ex:
    print("Error durante la conexión",ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexion ha finalizado")
