from socket import *
import time
ADDR = ('localhost', 21000)

srvsock = socket(AF_INET, SOCK_DGRAM)

srvsock.bind(ADDR)

hora = time.strftime("%H:%M:%S")
fecha = time.strftime("%d/%m/%y")
while True:
    print('esperando mensaje...')
    data, addr = srvsock.recvfrom(512)
    respuesta= (f"La hora del servidor es: {hora} y la fecha es {fecha}")
    srvsock.sendto(respuesta.encode(), addr)
    print('se recibio:', data.decode())
srvsock.close()
