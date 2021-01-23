import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import alumnos

class FormularioAlumnos():
    
    def __init__(self, username, password):
        self.alumno1=alumnos.Alumnos()
        self.ventana1=tk.Tk()
        self.ventana1.title("Alumnos")
        self.ventana1.resizable(False,False)
        self.ventana1.config(background = "#000000")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.carga_alumnos(username, password)
        #self.consulta_por_codigo()
        #self.listado_completo()
        #self.borrado()
        #self.modificar()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_alumnos(self, username, password):
        global usr
        global psswd
        self.usr = username
        self.psswd = password
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Cargar alumnos")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Alumno")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.control_var = StringVar(self.ventana1)
        self.name_var = StringVar(self.ventana1)
        self.last_var = StringVar(self.ventana1)
        self.crc_var = StringVar(self.ventana1)
        self.sem_var = StringVar(self.ventana1)
        
        self.label1= Label(self.labelframe1, text="Número de control:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.ent_control = Entry(self.labelframe1, textvariable = self.control_var)
        self.ent_control.grid(column=1, row=0, padx=4, pady=4)

        self.label2= Label(self.labelframe1, text="Nombre del alumno:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.ent_name = Entry(self.labelframe1, textvariable = self.name_var)
        self.ent_name.grid(column=1, row=1, padx=4, pady=4)
        
        self.label3= Label(self.labelframe1, text="Apellidos del alumno:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.ent_ap = Entry(self.labelframe1, textvariable = self.last_var)
        self.ent_ap.grid(column=1, row=2, padx=4, pady=4)
        
        self.label4= Label(self.labelframe1, text="Carrera:")
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.ent_car = Entry(self.labelframe1, textvariable = self.crc_var)
        self.ent_car.grid(column=1, row=3, padx=4, pady=4)
        
        self.label5= Label(self.labelframe1, text="Semestre:")        
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.ent_sem = Entry(self.labelframe1, textvariable = self.sem_var)
        self.ent_sem.grid(column=1, row=4, padx=4, pady=4)
        
        self.boton1= Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=5, padx=4, pady=4)

    def agregar(self):
        datos=(self.control_var.get(), self.name_var.get(), self.last_var.get(), self.crc_var.get(), self.sem_var.get(), self.usr, self.psswd)
        print(datos)
        #vald=self.alumno1.alta(datos)
        #if vald == True:
            #mb.showinfo("Información", "Los datos fueron cargados")
            #self.no_control.set("")
            #self.nombre_alumno.set("")
            #self.apellidos.set("")
            #self.carrera.set("")
            #self.semestre.set("")
        #else:
            #mb.showerror("Error", "Ya existe un alumno con dicho número de control")
            #self.no_control.set("")
            #self.nombre_alumno.set("")
            #self.apellidos.set("")
            #self.carrera.set("")
            #self.semestre.set("")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Alumno")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe2, text="Número de control:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        global entrycodigo
        self.entrycodigo=ttk.Entry(self.labelframe2)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe2, text="Nombre del alumno:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        global entrynombre
        self.entrynombre=ttk.Entry(self.labelframe2, state="readonly")
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe2, text="Apellidos del alumno:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        global entryapellido
        self.entryapellido=ttk.Entry(self.labelframe2, state="readonly")
        self.entryapellido.grid(column=1, row=2, padx=4, pady=4)
        self.label4=ttk.Label(self.labelframe2, text="Carrera:")        
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        global entrycarrera
        self.entrycarrera=ttk.Entry(self.labelframe2, state="readonly")
        self.entrycarrera.grid(column=1, row=3, padx=4, pady=4)
        self.label5=ttk.Label(self.labelframe2, text="Semestre:")        
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        global entrysemestre
        self.entrysemestre=ttk.Entry(self.labelframe2, state="readonly")
        self.entrysemestre.grid(column=1, row=4, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=5, padx=4, pady=4)

    def consultar(self):
        datos=(self.entrycodigo.get(), )
        respuesta=self.alumno1.consulta(datos)
        if len(respuesta)>0:
            self.nombre_alumno.set(respuesta[0][0])
            self.apellidos.set(respuesta[0][1])
            self.carrera.set(respuesta[0][2])
            self.semestre.set(respuesta[0][3])
        else:
            self.nombre_alumno.set('')
            self.apellidos.set('')
            self.carrera.set('')
            self.semestre.set('')
            mb.showerror("Error", "No existe un alumno con dicho código")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Alumno")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=50, height=20)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)
        self.boton2=ttk.Button(self.labelframe3, text="Exportar datos", command=self.documento)
        self.boton2.grid(column=0, row=2, padx=4, pady=4)

    def listar(self):
        respuesta=self.alumno1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "Número de control: "+str(fila[0])+"\nNombre del alumno: "+fila[2]+" "+fila[1]+"\nCarrera: "+str(fila[3])+"\nSemestre: "+str(fila[4])+"\n\n")

    def documento(self):
        result = mb.askquestion("Confirmar","¿Deseas exportar los datos a un archivo de texto?")
        if result == 'yes':
            respuesta2=self.alumno1.recuperar_todos()
            file = open("Alumnos_Inscritos.txt","w")
            for fila in respuesta2:
                file.write("Número de control: "+str(fila[0])+"\nNombre del alumno: "+fila[2]+" "+fila[1]+"\nCarrera: "+str(fila[3])+"\nSemestre: "+str(fila[4])+"\n\n")
            file.close
            mb.showinfo("Información", "El documento se creo con éxito")
        else:
            pass

    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de alumnado")
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Nombre")        
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe4, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe4, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe4, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos=(self.codigoborra.get(), )
        cantidad=self.alumno1.baja(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se borró el alumno con dicho código")
        else:
            mb.showerror("Error", "No existe un alumno con dicho código")

    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar alumno")
        self.labelframe5=ttk.LabelFrame(self.pagina5, text="Nombre")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe5, text="Número de control:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe5, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe5, text="Nombre del alumno:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombremod=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe5, textvariable=self.nombremod)
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe5, text="Apellidos:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.apellidosmod=tk.StringVar()
        self.entryapellidos=ttk.Entry(self.labelframe5, textvariable=self.apellidosmod)
        self.entryapellidos.grid(column=1, row=2, padx=4, pady=4)
        self.label4=ttk.Label(self.labelframe5, text="Carrera:")        
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.carreramod=tk.StringVar()
        self.entrycarrera=ttk.Entry(self.labelframe5, textvariable=self.carreramod)
        self.entrycarrera.grid(column=1, row=3, padx=4, pady=4)
        self.label5=ttk.Label(self.labelframe5, text="Semestre:")        
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.semestremod=tk.StringVar()
        self.entrysemestre=ttk.Entry(self.labelframe5, textvariable=self.semestremod)
        self.entrysemestre.grid(column=1, row=4, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=5, padx=4, pady=4)
        self.boton2=ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
        self.boton2.grid(column=1, row=6, padx=4, pady=4)

    def modifica(self):
        datos=(self.nombremod.get(), self.apellidosmod.get(), self.carreramod.get(), self.semestremod.get(), self.codigomod.get())
        cantidad=self.alumno1.modificacion(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el alumno")
        else:
            mb.showerror("Error", "No existe un alumno con dicho código")

    def consultar_mod(self):
        datos=(self.codigomod.get(), )
        respuesta=self.alumno1.consulta(datos)
        if len(respuesta)>0:
            self.nombremod.set(respuesta[0][0])
            self.apellidosmod.set(respuesta[0][1])
            self.carreramod.set(respuesta[0][2])
            self.semestremod.set(respuesta[0][3])
        else:
            self.nombremod.set('')
            self.apellidosmod.set('')
            self.carreramod.set('')
            self.semestremod.set('')
            mb.showerror("Información", "No existe un alumno con dicho código")
