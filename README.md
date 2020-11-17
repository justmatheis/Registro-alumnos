# Proyecto base de datos
Repositorio que almacenará los cambios y archivos para el proyecto de taller de base de datos.

# Importación
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
