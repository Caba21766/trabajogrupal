import tkinter as tk
from tkinter import *
ventana = Tk()
ventana.title("Mi primera Calculadora")
ventana.geometry("500x300")
etiqueta=Label(ventana, text="Documento:", font=("Arial",10)) .place(x=50,y=10)
etiqueta=Label(ventana, text="Apellido y Nombre:", font=("Arial",10)) .place(x=50,y=40)
etiqueta=Label(ventana, text="Domicilio:", font=("Arial",10)) .place(x=50,y=70)
etiqueta=Label(ventana, text="Edad:", font=("Arial",10)) .place(x=50,y=100)
etiqueta=Label(ventana, text="Num Celular:", font=("Arial",10)) .place(x=50,y=130)
boton = Button(ventana,text="Guardar").place(x=300,y=200)

entrada = tk.Entry(ventana, width=10, font=('Arial', 10), borderwidth=2, relief="solid").place(x=170,y=10)
entrada = tk.Entry(ventana, width=40, font=('Arial', 10), borderwidth=2, relief="solid").place(x=170,y=40)
entrada = tk.Entry(ventana, width=20, font=('Arial', 10), borderwidth=2, relief="solid").place(x=170,y=70)
entrada = tk.Entry(ventana, width=3, font=('Arial', 10), borderwidth=2, relief="solid").place(x=170,y=100)
entrada = tk.Entry(ventana, width=10, font=('Arial', 10), borderwidth=2, relief="solid").place(x=170,y=130)

ventana.mainloop()