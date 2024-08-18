# importamos las bibliotecas necesarias
# 
# +from tkinter import * 
from tkinter import ttk

# FUNCIONES 
# insertar elementos al treeview
def insertarElemento():
    producto=entProducto.get()
    descripcion=entDescripcion.get()
    cantidad=float(entCantidad.get())
    precio=float(entPrecioUnitario.get())
    subtotal=cantidad*precio
    

    trvGrilla.insert("",END, text=producto, values=(descripcion,cantidad,precio,subtotal))

# borrar campos
def borrarCampos():
    # entNumeroFactura.delete(0,END)
    entProducto.delete(0,END)
    entDescripcion.delete(0,END)
    entCantidad.delete(0,END)
    entPrecioUnitario.delete(0,END)
    


# creamos la ventanas con sus parametros
ventana=Tk()
ventana.geometry("800x600")
ventana.title("Sistema de Facturación")
ventana.resizable(0,0)


# crear los objetos de la ventana
# etiquetas Label

lblTitulo=Label(ventana, text="Sistema de Facturación", font=14)
lblTitulo.place(x=300, y=10)

lblNumeroFactura=Label(ventana, text="Nº Factura:")
lblNumeroFactura.place(x=10, y=50)

lblProducto=Label(ventana, text="Producto:")
lblProducto.place(x=10, y=90)

lblDescripcion=Label(ventana, text="Descripcion")
lblDescripcion.place(x=10, y=130)

lblCantidad=Label(ventana, text="Cantidad:")
lblCantidad.place(x=10, y=170)

lblPrecioUnitario=Label(ventana, text="Precio Unitario $:")
lblPrecioUnitario.place(x=10, y=210)

lblTotal=Label(ventana, text="Total $:")
lblTotal.place(x=600, y=500)

# cajas de texto Entry

entNumeroFactura=Entry(ventana, width=5 )
entNumeroFactura.place(x=130, y=50)

entProducto=Entry(ventana, width=50)
entProducto.place(x=130, y=90 )

entDescripcion=Entry(ventana,text="Descripción", width=50)
entDescripcion.place(x=130, y=130)

entCantidad=Entry(ventana, width=5)
entCantidad.place(x=130, y=170)

entPrecioUnitario=Entry(ventana, width=5)
entPrecioUnitario.place(x=130, y=210)

entTotal=Entry(ventana, width=8)
entTotal.place(x=690, y=500)

# creamos el treview 
trvGrilla=ttk.Treeview(ventana, columns=("Descripcion","Cantidad","Precio Unitario","Subtotal"))
trvGrilla.place(x=20, y=250, width=720)
trvGrilla.heading("#0", text="Producto")
trvGrilla.heading("Descripcion", text="Cantidad")
trvGrilla.heading("Cantidad", text="Cantidad")
trvGrilla.heading("Precio Unitario", text="Prec.Unit.")
trvGrilla.heading("Subtotal",text="Subtotal")

trvGrilla.column("#0",width=210,anchor=CENTER)
trvGrilla.column("#1",width=210, anchor=CENTER)
trvGrilla.column("#2",width=80, anchor=CENTER)
trvGrilla.column("#3",width=80,anchor=CENTER)
trvGrilla.column("#3",width=80,anchor=CENTER)

#sumar total
# Función para calcular el total de los subtotales
def actualizarTotal():
    total = 0
    for item in trvGrilla.get_children():
        subtotal = float(trvGrilla.item(item, 'values')[3])
        total += subtotal
    
    entTotal.delete(0, END)
    entTotal.insert(0, str(total))

# Modifica la función `insertarElemento` para incluir la actualización del total
def insertarElemento():
    producto = entProducto.get()
    descripcion = entDescripcion.get()
    cantidad = float(entCantidad.get())
    precio = float(entPrecioUnitario.get())
    subtotal = cantidad * precio
    
    trvGrilla.insert("", END, text=producto, values=(descripcion, cantidad, precio, subtotal))
    
    # Actualizar el total después de insertar el elemento
    actualizarTotal()

# creamos los botones
btnAgregar=Button(ventana, text="Agregar", width=12, command=insertarElemento)
btnAgregar.place(x=600, y=110)

btnBorrarCampos=Button(ventana, text="Borrar Campos", width=12, command=borrarCampos)
btnBorrarCampos.place(x=600, y=150)
ventana.mainloop()