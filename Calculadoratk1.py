import tkinter as tk
from tkinter import messagebox

def presionar_boton(valor):
    """Maneja las acciones de los botones de la calculadora."""
    if valor == "=":
        try:
            # Evalúa la expresión matemática en la entrada
            resultado = eval(entrada.get())
            entrada.delete(0, tk.END)  # Borra el contenido actual de la entrada
            entrada.insert(tk.END, str(resultado))  # Muestra el resultado
        except:
            # Muestra un mensaje de error si algo sale mal
            messagebox.showerror("Error", "Operación no válida")
            entrada.delete(0, tk.END)  # Borra el contenido en caso de error
    elif valor == "C":
        # Borra el contenido de la entrada
        entrada.delete(0, tk.END)
    else:
        # Añade el valor del botón a la entrada
        entrada.insert(tk.END, valor)

def presionar_enter(event):
    """Maneja la acción cuando se presiona Enter."""
    presionar_boton("=")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera Calculadora")

# Crear el campo de entrada
entrada = tk.Entry(ventana, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entrada.grid(row=0, column=0, columnspan=4)

# Asignar la función presionar_enter a la tecla Enter
entrada.bind('<Return>', presionar_enter)

# Definir los botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Crear y colocar los botones en la cuadrícula
for (texto, fila, columna) in botones:
    # Crear un botón en la interfaz gráfica
    boton = tk.Button(ventana, text=texto, width=4, height=2, font=('Arial', 18))
    boton.grid(row=fila, column=columna)
    
    # Asignar la función presionar_boton al evento de clic del botón
    boton.config(command=lambda t=texto: presionar_boton(t))

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()