import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

def validar():
    if username.get()=='ulises2' and str(password.get())=='1234567!':
        secundaria(username.get(),str(password.get()))
        print("Inicio de sesión correctos")
    else:
        messagebox.showwarning("ERROR","Contraseña o usuario incorrectos")

def conexion(username,password):
    try:
        conexion = mysql.connector.connect(
            host = 'db4free.net',
            port = 3306,
            user = username,
            password = password,
            db = 'proyectodb'
        )
    except Error as ex:
        print("Error durante la conexión",ex)
    if conexion.is_connected():
        print("Conexión exitosa a la base de datos")
    cursor = conexion.cursor()
    sql = "SELECT * FROM tabla_prueba"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def secundaria(user,password):
    second = Tk()
    frm = Frame(second)
    frm.pack(side=tk.LEFT, padx=110)

    tv = ttk.Treeview(frm, columns=(1,2), show="headings", height="3")
    tv.pack()

    tv.heading(1, text="ID")
    tv.heading(2, text="NOMBRE")

    rows = conexion(user,password)

    for i in rows:
        tv.insert('', 'end', values=i)
    
    second.title("FORMULARIO DE CONSULTAS")
    second.geometry("650x350")
    second.resizable(False,False)
    second.config(background = "#213141")
    second.mainloop()

mywindow = Tk()
mywindow.geometry("650x350")
mywindow.title("FORMULARIO DE INICIO")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = Label(text="FORMULARIO DE INICIO", font=("Cambria", 13), bg="#56CD63", fg="white", width="550", height="2")
main_title.pack()

username_label = Label(text="Usuario", bg="#FFEEDD")
username_label.place(x=300, y=70)
password_label = Label(text="Contraseña", bg="#FFEEDD")
password_label.place(x=295, y=150)

username = StringVar()
password = StringVar()

username_entry = Entry(textvariable=username, width="40")
password_entry = Entry(textvariable=password, width="40", show="*")

username_entry.place(x=200, y=100)
password_entry.place(x=200, y=180)

submit_btn = Button(mywindow, text="INICIAR SESION", command=validar, width="30", height="2", bg="#00CD63")
submit_btn.place(x=215, y=250)

mywindow.mainloop()
