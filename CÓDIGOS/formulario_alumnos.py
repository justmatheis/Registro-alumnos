import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import alumnos

my_entries = []

def inicio(user, passwd):     
    global alumno1
    alumno1=alumnos.Alumnos()
    global usuario
    usuario = user
    global contra
    contra = passwd
    ventana1=tk.Tk()
    ventana1.title("Alumnos")
    ventana1.resizable(False,False)
    ventana1.config(background = "#000000")
    global cuaderno1
    cuaderno1 = ttk.Notebook(ventana1)        
    carga_alumnos()
    consulta_por_codigo()
    #listado_completo()
    #borrado()
    #modificar()
    cuaderno1.grid(column=0, row=0, padx=10, pady=10)
    ventana1.mainloop()

def carga_alumnos():
    pagina1 = ttk.Frame(cuaderno1)
    cuaderno1.add(pagina1, text="Cargar alumnos")
    labelframe1=ttk.LabelFrame(pagina1, text="Alumno")        
    labelframe1.grid(column=0, row=0, padx=5, pady=10)
    
    global my_entry
        
    for x in range(5):
        my_entry = ttk.Entry(labelframe1)
        my_entry.grid(column=1, row=x, padx=4, pady=4)
        my_entries.append(my_entry)
    
    label1=ttk.Label(labelframe1, text="Número de control:")
    label1.grid(column=0, row=0, padx=4, pady=4)
        
    label2=ttk.Label(labelframe1, text="Nombre del alumno:")
    label2.grid(column=0, row=1, padx=4, pady=4)
    
    label3=ttk.Label(labelframe1, text="Apellidos del alumno:")
    label3.grid(column=0, row=2, padx=4, pady=4)
    
    label4=ttk.Label(labelframe1, text="Carrera:")
    label4.grid(column=0, row=3, padx=4, pady=4)
    
    label5=ttk.Label(labelframe1, text="Semestre:")        
    label5.grid(column=0, row=4, padx=4, pady=4)
    
    boton1=ttk.Button(labelframe1, text="Confirmar", command=agregar)
    boton1.grid(column=1, row=5, padx=4, pady=4)

def agregar():
    datos = []
    for i in range(5):
        datos.append(my_entries[i].get())
    datos.append(usuario)
    datos.append(contra)
    vald=alumno1.alta(datos)
    if vald == True:
        mb.showinfo("Información", "Los datos fueron cargados")
        my_entry.insert(0,'')
    else:
        mb.showerror("Error", "Ya existe un alumno con dicho número de control")
        my_entry.delete(0,'')

def consulta_por_codigo():
    pagina2 = ttk.Frame(cuaderno1)
    cuaderno1.add(pagina2, text="Consulta por código")
    labelframe2=ttk.LabelFrame(pagina2, text="Alumno")
    labelframe2.grid(column=0, row=0, padx=5, pady=10)
    label1=ttk.Label(labelframe2, text="Número de control:")
    label1.grid(column=0, row=0, padx=4, pady=4)
    global entrycode
    entrycode = ttk.Entry(labelframe2)
    entrycode.grid(column=1, row=0, padx=4, pady=4)
    
    global entrynombre
    label2=ttk.Label(labelframe2, text="Nombre del alumno:")        
    label2.grid(column=0, row=1, padx=4, pady=4)
    entrynombre=ttk.Entry(labelframe2, state="readonly")
    entrynombre.grid(column=1, row=1, padx=4, pady=4)
    
    apellidos = tk.StringVar()
    label3=ttk.Label(labelframe2, text="Apellidos del alumno:")        
    label3.grid(column=0, row=2, padx=4, pady=4)
    entryapellido=ttk.Entry(labelframe2, textvariable=apellidos, state="readonly")
    entryapellido.grid(column=1, row=2, padx=4, pady=4)
    
    carrera = tk.StringVar()
    label4=ttk.Label(labelframe2, text="Carrera:")        
    label4.grid(column=0, row=3, padx=4, pady=4)
    entrycarrera=ttk.Entry(labelframe2, textvariable=carrera, state="readonly")
    entrycarrera.grid(column=1, row=3, padx=4, pady=4)

    semestre = tk.StringVar()
    label5=ttk.Label(labelframe2, text="Semestre:")        
    label5.grid(column=0, row=4, padx=4, pady=4)
    entrysemestre=ttk.Entry(labelframe2, textvariable=semestre, state="readonly")
    entrysemestre.grid(column=1, row=4, padx=4, pady=4)
    
    boton1=ttk.Button(labelframe2, text="Consultar", command=consultar)
    boton1.grid(column=1, row=5, padx=4, pady=4)

def consultar():
    datos=(entrycode.get(), usuario, contra)
    respuesta=alumno1.consulta(datos)
    print()
    #if len(respuesta)>0:
        #entrynombre.insert(0,respuesta[0][0])
        #apellidos.set(respuesta[0][1])
        #carrera.set(respuesta[0][2])
        #semestre.set(respuesta[0][3])
    #else:
        #nombre_alumno.set('')
        #apellidos.set('')
        #carrera.set('')
        #semestre.set('')
        #mb.showerror("Error", "No existe un alumno con dicho código")

def listado_completo():
    pagina3 = ttk.Frame(cuaderno1)
    cuaderno1.add(pagina3, text="Listado completo")
    labelframe3=ttk.LabelFrame(pagina3, text="Alumno")
    labelframe3.grid(column=0, row=0, padx=5, pady=10)
    boton1=ttk.Button(labelframe3, text="Listado completo", command=listar)
    boton1.grid(column=0, row=0, padx=4, pady=4)
    global scrolledtext1
    scrolledtext1=st.ScrolledText(labelframe3, width=50, height=20)
    scrolledtext1.grid(column=0,row=1, padx=10, pady=10)
    boton2=ttk.Button(labelframe3, text="Exportar datos", command=documento)
    boton2.grid(column=0, row=2, padx=4, pady=4)

def listar():
    respuesta=alumno1.recuperar_todos()
    scrolledtext1.delete("1.0", tk.END)        
    for fila in respuesta:
        scrolledtext1.insert(tk.END, "Número de control: "+str(fila[0])+"\nNombre del alumno: "+fila[2]+" "+fila[1]+"\nCarrera: "+str(fila[3])+"\nSemestre: "+str(fila[4])+"\n\n")

def documento():
    result = mb.askquestion("Confirmar","¿Deseas exportar los datos a un archivo de texto?")
    if result == 'yes':
        respuesta2=alumno1.recuperar_todos()
        file = open("Alumnos_Inscritos.txt","w")
        for fila in respuesta2:
            file.write("Número de control: "+str(fila[0])+"\nNombre del alumno: "+fila[2]+" "+fila[1]+"\nCarrera: "+str(fila[3])+"\nSemestre: "+str(fila[4])+"\n\n")
        file.close
        mb.showinfo("Información", "El documento se creo con éxito")
    else:
        pass

def borrado():
    pagina4 = ttk.Frame(cuaderno1)
    cuaderno1.add(pagina4, text="Borrado de alumnado")
    labelframe4=ttk.LabelFrame(pagina4, text="Nombre")        
    labelframe4.grid(column=0, row=0, padx=5, pady=10)
    label1=ttk.Label(labelframe4, text="Código:")
    label1.grid(column=0, row=0, padx=4, pady=4)
    global codigoborra
    codigoborra=tk.StringVar()
    entryborra=ttk.Entry(labelframe4, textvariable=codigoborra)
    entryborra.grid(column=1, row=0, padx=4, pady=4)
    boton1=ttk.Button(labelframe4, text="Borrar", command=borrar)
    boton1.grid(column=1, row=1, padx=4, pady=4)

def borrar():
    datos=(codigoborra.get(), )
    cantidad=alumno1.baja(datos)
    if cantidad==1:
        mb.showinfo("Información", "Se borró el alumno con dicho código")
    else:
        mb.showerror("Error", "No existe un alumno con dicho código")

def modificar():
    pagina5 = ttk.Frame(cuaderno1)
    cuaderno1.add(pagina5, text="Modificar alumno")
    labelframe5=ttk.LabelFrame(pagina5, text="Nombre")
    labelframe5.grid(column=0, row=0, padx=5, pady=10)
    label1=ttk.Label(labelframe5, text="Número de control:")
    label1.grid(column=0, row=0, padx=4, pady=4)
    global codigomod
    codigomod=tk.StringVar()
    entrycodigo=ttk.Entry(labelframe5, textvariable=codigomod)
    entrycodigo.grid(column=1, row=0, padx=4, pady=4)
    label2=ttk.Label(labelframe5, text="Nombre del alumno:")        
    label2.grid(column=0, row=1, padx=4, pady=4)
    global nombremod
    nombremod=tk.StringVar()
    entrynombre=ttk.Entry(labelframe5, textvariable=nombremod)
    entrynombre.grid(column=1, row=1, padx=4, pady=4)
    label3=ttk.Label(labelframe5, text="Apellidos:")        
    label3.grid(column=0, row=2, padx=4, pady=4)
    global apellidosmod
    apellidosmod=tk.StringVar()
    entryapellidos=ttk.Entry(labelframe5, textvariable=apellidosmod)
    entryapellidos.grid(column=1, row=2, padx=4, pady=4)
    label4=ttk.Label(labelframe5, text="Carrera:")        
    label4.grid(column=0, row=3, padx=4, pady=4)
    global carreramod
    carreramod=tk.StringVar()
    entrycarrera=ttk.Entry(labelframe5, textvariable=carreramod)
    entrycarrera.grid(column=1, row=3, padx=4, pady=4)
    label5=ttk.Label(labelframe5, text="Semestre:")        
    label5.grid(column=0, row=4, padx=4, pady=4)
    global semestremod
    semestremod=tk.StringVar()
    entrysemestre=ttk.Entry(labelframe5, textvariable=semestremod)
    entrysemestre.grid(column=1, row=4, padx=4, pady=4)
    boton1=ttk.Button(labelframe5, text="Consultar", command=consultar_mod)
    boton1.grid(column=1, row=5, padx=4, pady=4)
    boton2=ttk.Button(labelframe5, text="Modificar", command=modifica)
    boton2.grid(column=1, row=6, padx=4, pady=4)

def modifica():
    datos=(nombremod.get(), apellidosmod.get(), carreramod.get(), semestremod.get(), codigomod.get())
    cantidad=alumno1.modificacion(datos)
    if cantidad==1:
        mb.showinfo("Información", "Se modificó el alumno")
    else:
        mb.showerror("Error", "No existe un alumno con dicho código")

def consultar_mod():
    datos=(codigomod.get(), )
    respuesta=alumno1.consulta(datos)
    if len(respuesta)>0:
        nombremod.set(respuesta[0][0])
        apellidosmod.set(respuesta[0][1])
        carreramod.set(respuesta[0][2])
        semestremod.set(respuesta[0][3])
    else:
        nombremod.set('')
        apellidosmod.set('')
        carreramod.set('')
        semestremod.set('')
        mb.showerror("Información", "No existe un alumno con dicho código")

