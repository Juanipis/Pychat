import tkinter as tk
import socket
import threading
from tkinter import messagebox



def recivir_mensajes(clientsocket, name, msg_list):
    # ------------------Recibir mesajes de chat--------------------------#
    while True:
        data = clientsocket.recv(1024)
        if not data: break
        data_msg = (name.decode('utf-8'), ': %s' % data.decode('utf-8'))
        msg_list.insert(tk.END, data_msg[0]+data_msg[1])
        #msg_list.insert(tk.END, data_msg[2])



def enviar_mensaje(entry_fiel, clientsocket, msg_list, user):
    msg = entry_fiel.get()
    msg_inlistbox = user, ': %s' %msg
    msg_list.insert(tk.END, msg_inlistbox[0]+msg_inlistbox[1])
    clientsocket.send(bytes(msg, "utf-8"))


# -------------------------------------------------SERVIDOR---------------------------------------------------------------------------------#

def server(ventanaPrincipal, user, ventana):
    ventana.destroy()

    # ------------------Variables de primer uso--------------------------#

    direccion_equipo = socket.gethostbyname(socket.gethostname())
    print(direccion_equipo)
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((direccion_equipo, 5151))  # Cambiar por local host por direccion equipo cuando vaya a hacer prueba entre dos pc con widows
    serversocket.listen(1)
    clientsocket, clientaddress = serversocket.accept()
    name = clientsocket.recv(1024)
    clientsocket.send(bytes(user, "utf-8"))

    # ------------------Mensajes de chat--------------------------#
    messages_frame = tk.Frame(ventanaPrincipal, height=150, width=150, bg="light blue")
    scrollbar = tk.Scrollbar(messages_frame)
    msg_list = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
    msg_list.pack()
    messages_frame.pack()

    # ------------------Recivir Mensajes de chat--------------------------#

    thread = threading.Thread(name='recivir', target=recivir_mensajes, args=(clientsocket, name, msg_list,))
    thread.start()

        # ------------------Enviar mesajes de chat--------------------------#

    entry_fiel = tk.Entry(ventanaPrincipal)
    send_buttom = tk.Button(ventanaPrincipal, text="Enviar",
                                command=lambda: enviar_mensaje(entry_fiel, clientsocket, msg_list, user))
    entry_fiel.pack()
    send_buttom.pack()


        #-----------------Protocolos de cierre---------------#

    def cerrando_conexion():
        if messagebox.askokcancel("Cerrar", "Realmente deseas cerrar?"):
            clientsocket.close()
            ventanaPrincipal.destroy()
            print("Exito de cierre de socket del servidor")

    ventanaPrincipal.protocol("WM_DELETE_WINDOW", cerrando_conexion)








# -------------------------------------------------CLIENTE---------------------------------------------------------------------------------#

def cliente(ventanaPrincipal, user, ventana):
    ventana.destroy()

    try:
        # ------------------Variables de primer uso--------------------------#
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        def empezar_cliente():
            try:
                clientsocket.send(bytes(user, "utf-8"))
                name = clientsocket.recv(1024)

                # ------------------Mensajes de chat--------------------------#
                messages_frame = tk.Frame(ventanaPrincipal, height=150, width=150, bg="light blue")
                scrollbar = tk.Scrollbar(messages_frame)
                msg_list = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
                msg_list.pack()
                messages_frame.pack()

                # ------------------Recivir Mensajes de chat--------------------------#

                thread = threading.Thread(name='recivir', target=recivir_mensajes, args=(clientsocket, name, msg_list,))
                thread.start()

                # ------------------Enviar mesajes de chat--------------------------#

                entry_fiel = tk.Entry(ventanaPrincipal)
                send_buttom = tk.Button(ventanaPrincipal, text="Enviar",
                                        command=lambda: enviar_mensaje(entry_fiel, clientsocket, msg_list, user))
                entry_fiel.pack()
                send_buttom.pack()

            except ConnectionResetError:
                ventanaPrincipal.destroy()

        def ingrsar_ip():
            i = 0
            while i <= 255:
                try:
                    clientsocket.connect(('192.168.1.%s' %i, 5151))
                    empezar_cliente()
                    break
                except TimeoutError:
                    i += 1
                    #ingrsar_ip(mensaje_ip, cajon_mensaje_ip, boton_mensaje_ip)
                    print('Error de conexion %s' %i)




        # -----------------Protocolos de cierre---------------#
        def cerrando_conexion():
            if messagebox.askokcancel("Cerrar", "Realmente deseas cerrar?"):
                clientsocket.close()
                ventanaPrincipal.destroy()
                print("Exito de cierre de socket del cliente")
        ventanaPrincipal.protocol("WM_DELETE_WINDOW", cerrando_conexion)

        ingrsar_ip()

    except ConnectionResetError:
        ventanaPrincipal.destroy()






def ventana_seleccion(ventanaPrincipal, user, ):
    ventana = tk.Toplevel(ventanaPrincipal)
    mensaje_bienvenida = tk.Label(ventana, text="Hola %s, ¿Como desea ingresar" % user).grid(row=0, column=1)
    boton_servidor = tk.Button(ventana, text="Servidor", command=lambda: server(ventanaPrincipal, user, ventana)).grid(
        row=1, column=0)
    boton_cliente = tk.Button(ventana, text="Cliente", command=lambda: cliente(ventanaPrincipal, user, ventana)).grid(
        row=1, column=2)
    nombre_equipo = socket.gethostname()
    direccion_equipo = socket.gethostbyname(nombre_equipo)
    mensaje_ip = tk.Label(ventana, text="Tu dirección ip es %s" % direccion_equipo).grid(row=2, column=1)
