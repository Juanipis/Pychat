from registro import registro
from ingreso import ingreso
import tkinter as tk

def inicio_ingreso(ventanaPrincipal, register_buttom, enter_buttom):
	register_buttom.pack_forget()
	enter_buttom.pack_forget()
	ingreso(ventanaPrincipal)



def root():
    ventanaPrincipal = tk.Tk()
    ventanaPrincipal.title("Pychat")
    register_buttom = tk.Button(ventanaPrincipal, text="Registro",
              command=lambda: registro(ventanaPrincipal), width=10)
    register_buttom.pack()
    enter_buttom = tk.Button(ventanaPrincipal, text="Ingreso",
              command=lambda: inicio_ingreso(ventanaPrincipal, register_buttom, enter_buttom), width=10)
    enter_buttom.pack()
    #tk.Button(ventanaPrincipal, text="prueba de cerrado",command=lambda:enter_buttom.pack_forget(), width=10).grid(row=1, column=1)
    ventanaPrincipal.mainloop()



    
root()