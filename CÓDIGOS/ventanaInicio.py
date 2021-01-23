import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from formulario_alumnos import FormularioAlumnos
import alumnos

class ventanaInicio:
    def __init__(self):
        self.mywindow = Tk()
        self.mywindow.geometry("650x350")
        self.mywindow.title("FORMULARIO DE INICIO")
        self.mywindow.resizable(False,False)
        self.mywindow.config(background = "#000000")
        self.main_title = Label(text="FORMULARIO DE INICIO", font=("Cambria", 13), bg="#B57EDC", fg="white", width="550", height="2")
        self.main_title.pack()

        self.username_label = Label(text="Usuario", bg="#FFEEDD")
        self.username_label.place(x=300, y=70)
        self.password_label = Label(text="Contraseña", bg="#FFEEDD")
        self.password_label.place(x=295, y=150)

        self.username = StringVar()
        self.password = StringVar()
        
        self.username_entry = Entry(self.mywindow, textvariable = self.username, width="40")
        self.password_entry = Entry(self.mywindow, textvariable = self.password, width="40", show="*")

        self.username_entry.place(x=200, y=100)
        self.password_entry.place(x=200, y=180)

        self.submit_btn = Button(self.mywindow, text="INICIAR SESION", command=self.validar, width="30", height="2", bg="#B57EDC", fg="white")
        self.submit_btn.place(x=215, y=250)

        self.mywindow.mainloop()

    def validar(self):
        self.alumno=alumnos.Alumnos()
        datos = (self.username.get(), self.password.get())
        #rst = self.alumno.conexionInicio(self.username.get(), self.password.get())
        if self.username.get() == 'Ulises':
            FormularioAlumnos(self.username.get(), self.password.get())
            #print("Exito")
            #self.mywindow.destroy()
        #print(datos)

ventanaInicio()
