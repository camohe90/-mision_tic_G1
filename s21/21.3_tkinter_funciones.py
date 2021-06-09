from tkinter import *

def mostrar_mensaje():
    mensaje.configure(text = "Estamos volando y nadie nos parara")


ventana = Tk()

mensaje = Label(ventana, fg="red", bg="white", font=("Arial bold", 14))
boton_mostrar = Button(ventana, text="Mostrar", command=mostrar_mensaje)
boton_cerrar = Button(ventana, text= "Cerrar", command= ventana.destroy)

mensaje.grid(row=0, column=0)
boton_mostrar.grid(row=1, column= 0)
boton_cerrar.grid(row=1, column=1) # 



ventana.mainloop()