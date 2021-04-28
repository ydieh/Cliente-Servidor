from socket import * #importamos la libreria socket
#creamos el objeto socket
socketServidor= socket(AF_INET,SOCK_STREAM)
#establecemos la coneccion con el metodo bind este recibe una tupla posee el host y el puerto donde esta escuchando
socketServidor.bind( ('localhost',21562) )
#establecemos la cantidad de peticiones que puedan estar en cola
socketServidor.listen(5)
# hacemos que siempre este escuchando el socket
while True:
    #aceptamos la conexion del cliente 
    socketCliente, addr = socketServidor.accept()# nos retorna dos valores la conexion y la direccion
    #imprimimos un msj cada vez q un cliente se conecte al servidor
    print ("Nueva conexion")
    #imprimimos la direccion de donde se conecto el cliente 
    print (addr)
    #recibimos el msj que nos envio el cliente
    # socket.recv(recv_size) recibe un mensaje TCP
    data = socketCliente.recv(200)
    print(data)
    #enviamos un msj al cliente
    socketCliente.send(b"hola desde servidor")
    #cerramos la conexion del cliente 
    socketCliente.close()
socketServidor.close()