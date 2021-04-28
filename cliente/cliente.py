from socket import *
ADDR = ('localhost', 21000)
cliSock = socket(AF_INET, SOCK_DGRAM)
data = "hola desde el cliente "
cliSock.sendto(data.encode("utf-8"), ADDR)
#recibimos el mensaje del servidor
data, ADDR = cliSock.recvfrom(512)
print(data.decode("utf-8"))
cliSock.close()
