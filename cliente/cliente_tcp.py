from socket import * #importamos la libreria socket
dest = ('localhost', 21562)
#creamos el socket cliente tcp
cliSock = socket(AF_INET, SOCK_STREAM)
#hacemos una conexion al servidor 
cliSock.connect(dest)
#creamos un msj
data = input('> ')
#enviamos el msj
cliSock.send(data.encode("utf-8"))
#recibimos el msj que el socket cliente
#hacemos referecia al buffer 1024 bytes
data = cliSock.recv(1024)
#mostramos el msj 
print(data.decode("utf-8"))
#cerramos el cliente 
cliSock.close()