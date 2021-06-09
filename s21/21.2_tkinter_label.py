from tkinter import *

ventana_ejemplo = Tk()

boton_cerrar = Button(ventana_ejemplo, text= "Cerrar", command= ventana_ejemplo.destroy)
mensaje = Label(ventana_ejemplo, text= "Seguimos avanzando con python")


mensaje.grid(row=0, column=0)
boton_cerrar.grid(row=0, column=1) # 

ventana_ejemplo.mainloop()