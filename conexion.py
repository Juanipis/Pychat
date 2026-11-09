import socket

def server(user1):
	nombre_equipo = socket.gethostname()
	direccion_equipo = socket.gethostbyname(nombre_equipo)
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.bind(('localhost', 5151))
	#print("La direccion del servidor es %s" %direccion_equipo, ":   Por favor pasela al cliente para iniciar chat")
	serversocket.listen(1)
	clientsocket, clientaddress = serversocket.accept()
	client_name = clientsocket.recv(1024)
	clientsocket.send(bytes(user1, "utf-8"))
	while 1:
		data = clientsocket.recv(1024) 
		print(client_name.decode('utf-8'), ': %s' %data.decode('utf-8'))  
		newdata = input('>') 
		clientsocket.send(bytes(newdata, "utf-8")) 
		if not newdata: break 
	clientsocket.close()

def client(user1):
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#direccion_server = input("Escriba la direccion ip del equipo al que se va conectar: ")
	clientsocket.connect(('localhost', 5151))
	clientsocket.send(bytes(user1, "utf-8"))
	server_name = clientsocket.recv(1024)
	while 1:
		data = input('>') 
		clientsocket.send(bytes(data, "utf-8")) 
		if not data: break 
		newdata = clientsocket.recv(1024) 
		print (server_name.decode('utf-8'),': %s' %newdata.decode('utf-8')) 
	clientsocket.close() 
