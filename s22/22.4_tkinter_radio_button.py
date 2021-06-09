from tkinter import *

# bloque de funciones
def mostrar_mensaje():
    nombre = info_entrada1.get()
    opcion = seleccion.get()
    if  opcion == 1:
        mensaje = "HOLA " + nombre
    elif opcion == 2:
        mensaje = "ADIOS " + nombre
    
    mensaje_salida.configure (text= mensaje)
        
# Defino mi variable ventana como el elemento principal de tkinter.
ventana = Tk()

info_entrada1 = StringVar()
seleccion = IntVar()

# Definir que elementos tiene mi interfaz grafica
entrada_texto = Entry(ventana, width=20, justify= CENTER, textvariable= info_entrada1)
mensaje_salida = Label(ventana, fg="red", bg="white", font=("Arial",))
boton_saludar = Radiobutton(ventana, text="hola", variable = seleccion, value =1, command=mostrar_mensaje)
boton_despedir = Radiobutton(ventana, text="adios", variable = seleccion, value =2, command=mostrar_mensaje)
boton_cerrar = Button(ventana, text="Cerrar", command=ventana.destroy)

# Ubicar los elementos en la pantalla
entrada_texto.grid(row=0, column=0)
mensaje_salida.grid(row=1, column=0)
boton_saludar.grid(row=1, column=1)
boton_despedir.grid(row=1, column=2)
boton_cerrar.grid(row=1, column=3)

# Sin esto no funciona
ventana.mainloop()