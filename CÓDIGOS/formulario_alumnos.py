import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import alumnos

def inicio():     
    global alumno1
    alumno1=alumnos.Alumnos()
    ventana1=tk.Tk()
    ventana1.title("Alumnos")
    ventana1.resizable(False,False)
    ventana1.config(background = "#000000")
    global cuaderno1
    cuaderno1 = ttk.Notebook(ventana1)        
    carga_alumnos()
    consulta_por_codigo()
    listado_completo()
    borrado()
    modificar()
    cuaderno1.grid(column=0, row=0, padx=10, pady=10)
    ventana1.mainloop()

def carga_alumnos():
    pagina1 = ttk.Frame(cuaderno1)
    cuaderno1.add(pagina1, text="Cargar alumnos")
    labelframe1=ttk.LabelFrame(pagina1, text="Alumno")        
    labelframe1.grid(column=0, row=0, padx=5, pady=10)
    label1=ttk.Label(labelframe1, text="Número de control:")
    label1.grid(column=0, row=0, padx=4, pady=4)
    global no_control
    no_control=tk.StringVar()
    entrycontrol=ttk.Entry(labelframe1, textvariable=no_control)
    entrycontrol.grid(column=1, row=0, padx=4, pady=4)
    label2=ttk.Label(labelframe1, text="Nombre del alumno:")
    label2.grid(column=0, row=1, padx=4, pady=4)
    global nombre_alumno
    nombre_alumno=tk.StringVar()
    entrynombre=ttk.Entry(labelframe1, textvariable=nombre_alumno)
    entrynombre.grid(column=1, row=1, padx=4, pady=4)
    label3=ttk.Label(labelframe1, text="Apellidos del alumno:")
    label3.grid(column=0, row=2, padx=4, pady=4)
    global apellidos
    apellidos=tk.StringVar()
    entryapellido=ttk.Entry(labelframe1, textvariable=apellidos)
    entryapellido.grid(column=1, row=2, padx=4, pady=4)
    label4=ttk.Label(labelframe1, text="Carrera:")
    label4.grid(column=0, row=3, padx=4, pady=4)
    global carrera
    carrera=tk.StringVar()
    entrycarrera=ttk.Entry(labelframe1, textvariable=carrera)
    entrycarrera.grid(column=1, row=3, padx=4, pady=4)
    label5=ttk.Label(labelframe1, text="Semestre:")        
    label5.grid(column=0, row=4, padx=4, pady=4)
    global semestre
    semestre=tk.StringVar()
    entrysemestre=ttk.Entry(labelframe1, textvariable=semestre)
    entrysemestre.grid(column=1, row=4, padx=4, pady=4)
    boton1=ttk.Button(labelframe1, text="Confirmar", command=agregar)
    boton1.grid(column=1, row=5, padx=4, pady=4)

def agregar():
    datos=(no_control.get(), nombre_alumno.get(), apellidos.get(), carrera.get(), semestre.get())
    vald=alumno1.alta(datos)
    if vald == True:
        mb.showinfo("Información", "Los datos fueron cargados")
        no_control.set("")
        nombre_alumno.set("")
        apellidos.set("")
        carrera.set("")
        semestre.set("")
    else:
        mb.showerror("Error", "Ya existe un alumno con dicho número de control")
        no_control.set("")
        nombre_alumno.set("")
        apellidos.set("")
        carrera.set("")
        semestre.set("")

def consulta_por_codigo():
    pagina2 = ttk.Frame(cuaderno1)
    cuaderno1.add(pagina2, text="Consulta por código")
    labelframe2=ttk.LabelFrame(pagina2, text="Alumno")
    labelframe2.grid(column=0, row=0, padx=5, pady=10)
    label1=ttk.Label(labelframe2, text="Número de control:")
    label1.grid(column=0, row=0, padx=4, pady=4)
    entrycodigo=ttk.Entry(labelframe2, textvariable=no_control)
    entrycodigo.grid(column=1, row=0, padx=4, pady=4)
    label2=ttk.Label(labelframe2, text="Nombre del alumno:")        
    label2.grid(column=0, row=1, padx=4, pady=4)
    entrynombre=ttk.Entry(labelframe2, textvariable=nombre_alumno, state="readonly")
    entrynombre.grid(column=1, row=1, padx=4, pady=4)
    label3=ttk.Label(labelframe2, text="Apellidos del alumno:")        
    label3.grid(column=0, row=2, padx=4, pady=4)
    entryapellido=ttk.Entry(labelframe2, textvariable=apellidos, state="readonly")
    entryapellido.grid(column=1, row=2, padx=4, pady=4)
    label4=ttk.Label(labelframe2, text="Carrera:")        
    label4.grid(column=0, row=3, padx=4, pady=4)
    entrycarrera=ttk.Entry(labelframe2, textvariable=carrera, state="readonly")
    entrycarrera.grid(column=1, row=3, padx=4, pady=4)
    label5=ttk.Label(labelframe2, text="Semestre:")        
    label5.grid(column=0, row=4, padx=4, pady=4)
    entrysemestre=ttk.Entry(labelframe2, textvariable=semestre, state="readonly")
    entrysemestre.grid(column=1, row=4, padx=4, pady=4)
    boton1=ttk.Button(labelframe2, text="Consultar", command=consultar)
    boton1.grid(column=1, row=5, padx=4, pady=4)

def consultar():
    datos=(no_control.get(), )
    respuesta=alumno1.consulta(datos)
    if len(respuesta)>0:
        nombre_alumno.set(respuesta[0][0])
        apellidos.set(respuesta[0][1])
        carrera.set(respuesta[0][2])
        semestre.set(respuesta[0][3])
    else:
        nombre_alumno.set('')
        apellidos.set('')
        carrera.set('')
        semestre.set('')
        mb.showerror("Error", "No existe un alumno con dicho código")

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

inicio()
