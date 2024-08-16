import tkinter as tk
#from tkinter import messagebox

def saludar():
    print("hola")

ventana = tk.Tk()
ventana.title("Mi primera Calculadora")
ventana.geometry("400x300")
etiqueta=tk.Label(ventana, text="hola mundo", font=("Arial",20))
etiqueta.pack()

Boton1=tk.Button(ventana, text="saludar", font=("Arial", 20), command=saludar)
Boton2=tk.Button(ventana, text="saludar", font=("Arial", 20), command=saludar)
Boton3=tk.Button(ventana, text="saludar", font=("Arial", 20), command=saludar)

Boton1.pack(side="left")
Boton2.pack(side="left")
Boton3.pack(side="right")

ventana.mainloop()

