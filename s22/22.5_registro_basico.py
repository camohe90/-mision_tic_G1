from tkinter import *
clientes = []


def guardar_datos():
    nombre = info_nombre.get()
    apellido = info_apellido.get()
    cedula = info_cedula.get()
    clientes.append(nombre + " " + apellido + " " + cedula)
    mensaje["text"] = "Cliente guardado"

ventana = Tk()
ventana.geometry('800x600')


nombre = Label(ventana, text= "Nombre: ")
apellido = Label(ventana, text= "Apellido: ")
cedula = Label(ventana, text= "Cedula: ")

info_nombre = StringVar()
info_apellido = StringVar()
info_cedula = StringVar()

entrada_nombre = Entry(ventana, width=25, justify= LEFT, textvariable= info_nombre)
entrada_apellido = Entry(ventana, width=25, justify= LEFT, textvariable= info_apellido)
entrada_cedula = Entry(ventana, width=25, justify= LEFT, textvariable= info_cedula)

boton_guardar = Button(ventana, text="Guardar", command=guardar_datos)
mensaje = Label(ventana, fg ="red")


nombre.grid(row=0, column=0)
apellido.grid(row=1, column=0)
cedula.grid(row=2, column=0)
entrada_nombre.grid(row=0,column=1)
entrada_apellido.grid(row=1,column=1)
entrada_cedula.grid(row=2,column=1)
boton_guardar.grid(row=3, column=0)
mensaje.grid(row=4, column=0)


ventana.mainloop()