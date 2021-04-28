from socket import *
dest = ('192.241.136.170', 80)
cliSock = socket(AF_INET, SOCK_STREAM)
cliSock.connect(dest)

pregunta = 'GET http://data.pr4e.org/intro.txt HTTP/1.0\r\n\r\n'
cliSock.send(pregunta.encode())
data =b""
#http ok bad res
#servidor unisx
#<h1>
#vnjfvjfj
while True:
    respuesta = cliSock.recv(5200)
    if(len(respuesta)< 1):
        break
    data = data + respuesta
cliSock.close()
print (data.decode('utf-8'))

