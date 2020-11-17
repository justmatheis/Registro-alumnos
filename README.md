# Proyecto base de datos
Repositorio que almacenará los cambios y archivos para el proyecto de taller de base de datos.

# Conexión
```python
  # Importamos la libreria de mysql para python
  # Desde la misma libreria importamos el objeto Error
  # por si se presenta errores en la conexión
  import mysql.connector
  from mysql.connector import Error
```
# Parametros
```python
    # Instaciamos un objeto "conexión" de la clase mysql.connector.connect
    # y enviamos los siguientes parametros
    conexion = mysql.connector.connect(
        host = 'db4free.net', # Nombre del servidor o host
        port = 3306, # El puerto que por defecto es 3306
        user = 'ulises2', # Usuario o nombre del superusuario que controla el gestor
        password = '1234567!', # La contraseña
        db = 'proyectodb' # Nombre en especifico de la base de datos
    )
```
