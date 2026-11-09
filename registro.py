import tkinter as tk

def registro_user_password(user, password, ventana_Registro):
    user = user.get()
    password = password.get()
    archivo = open('usuarios.txt', 'a')
    user_register = (user, password)
    archivo.write(str(user_register))
    archivo.write("\n")
    archivo.close()
    ventana_Registro.destroy()


def registro(ventanaPrincipal):
    ventana_Registro = tk.Toplevel(ventanaPrincipal)
    ventana_Registro.title("Registro")
    tk.Label(ventana_Registro, text="Escribe tu usuario").grid(row=0, column=0)
    tk.Label(ventana_Registro, text="Escribe tu contraseña").grid(row=1, column=0)
    user = tk.Entry(ventana_Registro)
    user.grid(row=0, column=2)
    password = tk.Entry(ventana_Registro)
    password.grid(row=1, column=2)
    tk.Button(ventana_Registro, text="Registrate", 
    	command=lambda: registro_user_password(user, password, ventana_Registro)).grid(row=2, column=1)