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

# Requisitos previos:
Desde el explorador de archivos de windows entrar a la siguiente ruta:

        C:\Users\nombre_de_usuario\AppData\Local\Programs\Python\Python39

Dentro de la ruta, dar shift+clic_derecho y seleccionar la opción "Abrir la ventana de PowerShell aquí"

Ejecutamos los siguientes comandos:
```
  > python -m pip install --upgrade pip setuptools wheel
  > pip install mysql-connector-python
```
# Interfaces gráficas:
Importamos la librerias necesarias.
```python
  import tkinter as tk
  from tkinter import *
  from tkinter import messagebox
  from tkinter import ttk #Liberias usadas para mostrar interfaces
  import mysql.connector
  from mysql.connector import Error #Liberias para la conexión a la base de datos
```

Creamos las vistas, mediante la libreria TKINTER (Ventana principal).
```python
  mywindow = Tk() #Llamado al método TKINTER
  mywindow.geometry("650x350") #Dimensiones
  mywindow.title("FORMULARIO DE INICIO") #Titulo de la ventana
  mywindow.resizable(False,False)
  mywindow.config(background = "#213141")
  main_title = Label(text="FORMULARIO DE INICIO", font=("Cambria", 13), bg="#56CD63", fg="white", width="550", height="2")
  main_title.pack()

  username_label = Label(text="Usuario", bg="#FFEEDD") #Etiquetas
  username_label.place(x=300, y=70) #Colocamos las etiquetas en el formulario
  password_label = Label(text="Contraseña", bg="#FFEEDD")
  password_label.place(x=295, y=150)

  username = StringVar() #Declaramos variables
  password = StringVar()
  
  username_entry = Entry(textvariable=username, width="40") #Creamos los campos de texto
  password_entry = Entry(textvariable=password, width="40", show="*")

  username_entry.place(x=200, y=100) #Colocamos los campos de texto al formulario
  password_entry.place(x=200, y=180)

  submit_btn = Button(mywindow, text="INICIAR SESION", command=validar, width="30", height="2", bg="#00CD63") #Creamos un botón para enviar los datos llaciendo llamado al metodo validar
  submit_btn.place(x=215, y=250) #Colocamos el botón en el formulario

  mywindow.mainloop()
```

Metodo que valida el correo y contraseña.
```python
  def validar():
    if username.get()=='ulises2' and str(password.get())=='1234567!': #Verificamos si el usuario y contraseña sean correctos
        secundaria(username.get(),str(password.get())) #Enviamos los parametros del nombre y usuario a la segunda ventana
        print("Inicio de sesión correctos") #Se imprime un mensaje en consola
    else:
        messagebox.showwarning("ERROR","Contraseña o usuario incorrectos") #Abrimos la ventana emergente de error
```

Método de conexión.
```python
  def conexion(username,password):
    try:
        conexion = mysql.connector.connect(
            host = 'db4free.net',
            port = 3306,
            user = username, #Enviamos el parametro del usuario
            password = password, #Parametro de la contraseña
            db = 'proyectodb'
        )
    except Error as ex:
        print("Error durante la conexión",ex) #Si se presenta el error en la conexión, imprimimos el siguiente mensaje
    if conexion.is_connected():
        print("Conexión exitosa a la base de datos") #Imprimimos un mensaje en consola
    cursor = conexion.cursor() #Creamos un cursor de conexión
    sql = "SELECT * FROM tabla_prueba" #Creamos la sentencia mysql que ejecutará el cursor
    cursor.execute(sql) #Ejecutamos la sentencia mysql
    rows = cursor.fetchall() #Guardamos los datos de la tabla en un vector
    return rows #Retornamos el vector
```

Ventana secundaria.
```python
  def secundaria(user,password): #Recibe parametros
    second = Tk()
    frm = Frame(second) #Convertimos la ventana en un objeto de tipo frame 
    frm.pack(side=tk.LEFT, padx=110) #Creamos un objeto donde se mostrará la tabla

    tv = ttk.Treeview(frm, columns=(1,2), show="headings", height="3") #Mostramos la tabla mediante una vista de arbol
    tv.pack()
 
    tv.heading(1, text="ID") #Nombre de las columnas
    tv.heading(2, text="NOMBRE")

    rows = conexion(user,password) #Llamamos al metodo conexion y guardamos el resultado de este

    for i in rows:
        tv.insert('', 'end', values=i) #Insertamos dentro de la vista los valores del vector
    
    second.title("FORMULARIO DE CONSULTAS") #Titulo de la ventana
    second.geometry("650x350") #Dimensiones
    second.resizable(False,False) 
    second.config(background = "#213141") #Fondo
    second.mainloop()
```




