#importamos la libreria socket para la creacion del socket servidor
from socket import *
#importamos la libreria time para enviar la hora 
ADDR = ('localhost', 21566)
#creamos el servidor udp
srvsock = socket(AF_INET, SOCK_DGRAM)
#establecemos la conexion con el metodo bind 
srvsock.bind(ADDR)
while True:
 print('esperando mensaje...')
 #aceptamos las conexiones de los clientes
 data, addr = srvsock.recvfrom(5120)

 #mostramos el msj q nos envio el cliente 
 cadena = data.decode("utf-8")
 numero = int (cadena)
 print('se recibio:', numero)
srvsock.close()