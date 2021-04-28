import socket 

host , port = '127.0.0.1' , 5300

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#seteamos el server socket 
serversocket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
#ponemos a escuchar el socket 
serversocket.bind((host , port))
#ponemos a escuchar al servidor
serversocket.listen(1)
print('servidor en el puerto',port)

while True:
    #aceptamos las conexiones de los clientes 
    connection , address = serversocket.accept()
    #recibimos los datos del cliente 
    data = connection.recv(1024).decode('utf-8')
    #separamos los datos con cada espacio y lo guardamos en una lista 
     string_list = request.split(' ')
    #guardamos la primera posicion de la lista en la variable method ej localhost:8888
    method = string_list[0]
    #guardamos la segunda parte de la lista en request_file eje /img
    requesting_file = string_list[1]
    #mostramos que es lo que requiere el cliente
    print('Client request',requesting_file)
    #si cada vez que halla un ? en lo que requiere el cliente no tengra ninguna relevancia
    myfile = requesting_file.split('?')[0]
    #obtenemos la direccion que requiere el cliente 
    myfile = myfile.lstrip('/')
    #si no requiere ningun archivo mostramos el index.html pero aun no lo leemos
    if(myfile == ''):
        myfile = 'index.html'
    #hacemos un try cath para el manejo de errores
    try:
        # abrimos el archivo Leemos el archivo rb(read byte)
        file = open(myfile , 'rb')
        response = file.read()
        #cerramos el archivo
        file.close()
        #creamos una cabecera para responder al cliente
        header = 'HTTP/1.1 200 OK\n'
        #escribimos en el tipo de contenido
       if(myfile.endswith('.jpg')):
            mimetype = 'image/jpg'
        elif(myfile.endswith('.css')):
            mimetype = 'text/css'
        elif(myfile.endswith('.pdf')):
            mimetype = 'application/pdf'
        else:
            mimetype = 'text/html'
        #concatenamos el header con el content type
        header += 'Content-Type: '+str(mimetype)+'\n\n'

    except Exception as e:
        #si exite un error mostramos el 404
        print("-")
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body>Error 404: File not found</body></html>'.encode('utf-8')
    #definimos la respuesta  con la cabecera
    final_response = header.encode('utf-8')
    #lo concatenamos con la respuesta
    final_response += response
    #enviamos la respuesta
    connection.send(final_response)
    connection.close()
