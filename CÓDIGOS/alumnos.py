import mysql.connector
from mysql.connector import Error

class Alumnos:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="Ulises125", 
                                              database="mi_proyecto") #Objeto de la clase connect que envia los datos de la base de datos
        return conexion 


    def alta(self, datos):
        try: #Método try-catch
            cone=self.abrir() #Llamado al método que realiza la conexión
            cone.autocommit = False #Autocommit igual a 0
            cursor=cone.cursor() #Crea cursor a la base de datos
            sql="insert into alumnos(no_control, nombre, apellidos, carrera, semestre) values (%s,%s,%s,%s,%s)" #Insertamos datos a la tabla creada
            cursor.execute(sql, datos) #Ejecutamos la sentencia en el gestor
            cone.commit() #Fin del modo transaccional
            cone.close() #Cierra la conexión
            return True #Retorna verdadero si se completo correctamente
        except mysql.connector.Error as error:
            cone.rollback() #Método que hace rollback a la última sentencia
            return False #Retorna falso si se completo correctamente

    def consulta(self, datos):
        cone=self.abrir() 
        cursor=cone.cursor()
        sql="select nombre, apellidos, carrera, semestre from alumnos where no_control=%s" #Sentencia que retorna todos los datos dependiendo del identificador
        cursor.execute(sql, datos)
        return cursor.fetchall() #Retorna el vector que contiene los datos consultados

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select * from alumnos" #Retorna todos los datos de la tabla
        cursor.execute(sql)
        return cursor.fetchall()

    def baja(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from alumnos where no_control=%s" #Borra las columnas con dicho número de control
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount #Retornar la cantidad de filas borradas
        except mysql.connector.Error as error:
            cone.rollback()
            return cursor.rowcount

    def modificacion(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update alumnos set nombre=%s, apellidos=%s, carrera=%s, semestre=%s where no_control=%s" #Actualiza los datos de las columnas
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount #Retornar la cantidad de filas modificadas
        except mysql.connector.Error as error:
            cone.rollback()
            return cursor.rowcount
