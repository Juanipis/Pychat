from registro import registro
from ingreso import ingreso
import tkinter as tk

def inicio_ingreso(ventanaPrincipal, register_buttom, enter_buttom, mensaje_bienvenida_instrucciones, mensaje_bienvenida):
    mensaje_bienvenida_instrucciones.pack_forget()
    mensaje_bienvenida.pack_forget()
    register_buttom.pack_forget()
    enter_buttom.pack_forget()
    ingreso(ventanaPrincipal)



def root():
    ventanaPrincipal = tk.Tk()
    ventanaPrincipal.title("Pychat")
    mensaje_bienvenida = tk.Label(ventanaPrincipal, text='Bienvenido a Pychat', font=('Arial', 20), padx=20, pady=5)
    mensaje_bienvenida.pack()
    mensaje_bienvenida_instrucciones = tk.Label(ventanaPrincipal, text='Un chat de escritorio programado en Python por Juan Pablo Díaz Correa, para usarlo regístrate o ingresa con un usuario y contraseña, \n seleccione la modalidad de servidor para escuchar a solicitudes de mensajería por parte de otros dispositivos', padx=20, pady=5)
    mensaje_bienvenida_instrucciones.pack()
    register_buttom = tk.Button(ventanaPrincipal, text="Registro",
              command=lambda: registro(ventanaPrincipal), width=15)
    register_buttom.pack(side = tk.LEFT)
    enter_buttom = tk.Button(ventanaPrincipal, text="Ingreso",
              command=lambda: inicio_ingreso(ventanaPrincipal, register_buttom, enter_buttom, mensaje_bienvenida_instrucciones, mensaje_bienvenida), width=15)
    enter_buttom.pack(side = tk.RIGHT)
    ventanaPrincipal.mainloop()


root()