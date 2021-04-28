#importamos la libreria socket
from socket import *
# definimos el host y el puerto 
ADDR = ('localhost', 21566)
#creamos el socket cliente
cliSock = socket(AF_INET, SOCK_DGRAM)
#leemos datos por consola 
data = input('> ')
#enviamos datos al servidor
cliSock.sendto(data.encode("utf-8"), ADDR)
#recivimos el datagrama  del servidor
data, ADDR = cliSock.recvfrom(512)
#mostramos los datos que nos envio el cliente
print(data.decode("utf-8"))
cliSock.close()
