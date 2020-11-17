# Proyecto base de datos
Repositorio que almacenará los cambios y archivos para el proyecto de taller de base de datos.
Para ingresar a la base de datos en la nube usada para este ejemplo:

1.- Ingresamos a: https://www.db4free.net/signup.php

2.- En la parte izquierda seleccionamos la opción phpMyAdmin

4.- Dentro de la ventana de inicio de phpMyAdmin, ingresamos el usuario: ulises2 y la contraseña 1234567!

5.- Ejecutamos el código y listo:)

# Importación
Librerias usadas en el script
```python
  # Importamos la libreria de mysql para python
  # Desde la misma libreria importamos el objeto Error
  # por si se presenta errores en la conexión
  import mysql.connector
  from mysql.connector import Error
```
# Conexión

Parametros/Instancia
```python
    # Instanciamos un objeto "conexión" de la clase mysql.connector.connect
    # y enviamos los siguientes parametros
    conexion = mysql.connector.connect(
        host = 'db4free.net', # Nombre del servidor o host
        port = 3306, # El puerto que por defecto es 3306
        user = 'ulises2', # Usuario o nombre del superusuario que controla el gestor
        password = '1234567!', # La contraseña
        db = 'proyectodb' # Nombre en especifico de la base de datos
    )
```

Condicional que verifica que la conexión se cumpla
```python
  # Llamado a la clase is_connected de la clase mysql.connector
  if conexion.is_connected():
        print("Conexión exitosa") # Si la conexión es exitosa se cumple la condición
        infoServer = conexion.get_server_info() # Llamado a la clase get_server_info 
        print("Info del servidor: ",infoServer) # Información del servidor en el que se hostea
        cursor = conexion.cursor() # Creamos un objeto de la clase cursor para seleccionar datos
        cursor.execute("SELECT database()") # Llamado al metodo execute, el parametro es en comillas ya que se envia una cadena de texto que recibirá el gestor
```
        
Selección de datos
```python
  registro = cursor.fetchone() # Creamos un objeto de la clase fetchone que indica que solo se obtendrá un valor de una tabla
  print("Conectado a la base de datos ",registro) # Imprimimos el valor de la variable que guarda el nombre de la base de datos
  cursor.execute("SELECT * FROM tabla_prueba") # Eejecutamos la sentencia que le mandaremos al gestor
  resultados = cursor.fetchall() # Indica que se mostrarán diversos objetos de una tabla
  for fila in resultados: # Ciclo for para mostrar los datos almacenados en un vector por cada registro
    print("Número de estudiante: ",fila[0]) # Imprimimos el valor 1 del vetor
    print("Nombre del estudiante: ",fila[1]) # ...
    print("Edad del estudiante: ",fila[2]) # ...
    print("Carrera: ",fila[3]) # Hasta el valor n del vector
```
# Método try-except
Sentencia except
```python
  # Arroja la excepción si se encuentra un error en la conexión
  except Error as ex:
    print("Error durante la conexión",ex) # Imprime el error especifico
```  
Sentencia finally
```python
  # Método finally que se cumple si hay error o no en la conexión
  # Es importante finalizar/cerrar la conexión a la base de datos 
  finally:
    if conexion.is_connected(): # Llamado al método is_connected
      conexion.close() # Cerramos la conexión
      print("La conexion ha finalizado") # Imprimos un mensaje de aviso
```
