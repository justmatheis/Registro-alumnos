import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import formulario_alumnos
import alumnos

def inicio():
    mywindow = Tk()
    mywindow.geometry("650x350")
    mywindow.title("FORMULARIO DE INICIO")
    mywindow.resizable(False,False)
    mywindow.config(background = "#000000")
    main_title = Label(text="FORMULARIO DE INICIO", font=("Cambria", 13), bg="#B57EDC", fg="white", width="550", height="2")
    main_title.pack()

    username_label = Label(text="Usuario", bg="#FFEEDD")
    username_label.place(x=300, y=70)
    password_label = Label(text="Contraseña", bg="#FFEEDD")
    password_label.place(x=295, y=150)

    global username_entry
    global password_entry
        
    username_entry = Entry(mywindow, width="40")
    password_entry = Entry(mywindow, width="40", show="*")

    username_entry.place(x=200, y=100)
    password_entry.place(x=200, y=180)

    submit_btn = Button(mywindow, text="INICIAR SESION", command=validar, width="30", height="2", bg="#B57EDC", fg="white")
    submit_btn.place(x=215, y=250)

    mywindow.mainloop()

def validar():
    alumno = alumnos.Alumnos()
    vald = alumno.conexionInicio(username_entry.get(), password_entry.get())
    if vald == True:
        formulario_alumnos.inicio(username_entry.get(), password_entry.get())

inicio()
