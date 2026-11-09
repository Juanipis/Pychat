import tkinter as tk
from chat import ventana_seleccion

def ingreso_user_password(user, password, ventana_Ingreso, ventanaPrincipal):
    user = user.get()
    password = password.get()
    archivo = open('usuarios.txt', 'r')
    registered = archivo.read()
    user_password = (user, password)
    validate = registered.find(str(user_password))
    archivo.close()
    if validate >= 0:
        ventana_Ingreso.destroy()
        ventana_seleccion(ventanaPrincipal, user,)


    else:
        tk.Label(ventana_Ingreso, text="Usuario y contraseña incorrectos, por favor intentelo de nuevo",
                 fg="red").grid(row=3, column=1)
    
        

def ingreso(ventanaPrincipal):
    ventana_Ingreso = tk.Toplevel(ventanaPrincipal)
    ventana_Ingreso.title("Ingreso")
    tk.Label(ventana_Ingreso, text="Escribe tu usuario").grid(row=0, column=0)
    tk.Label(ventana_Ingreso, text="Escribe tu contraseña",).grid(row=1, column=0)
    user = tk.Entry(ventana_Ingreso)
    user.grid(row=0, column=2)
    password = tk.Entry(ventana_Ingreso)
    password.grid(row=1, column=2)
    tk.Button(ventana_Ingreso, text="Ingresa", 
    	command=lambda: ingreso_user_password(user, password, ventana_Ingreso, ventanaPrincipal)).grid(row=2, column=1)
