from socket import *
# Welcome socket
serverSocket = socket(AF_INET, SOCK_STREAM)
# Attach port number 8008 to this welcome socket
serverSocket.bind(('', 8008))
# Set the max connections
serverSocket.listen(1)
while True:
    print("The server is ready to serve!")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(4096)
        filename = message.split()[1]
        filename = filename[1:]
        with open(filename, 'r', encoding='utf-8') as f:
            output = f.read()
        header = "HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: {}\r\n".format(len(output))
        body = output
        content = "{}\r\n{}".format(header, body)
        connectionSocket.send(content.encode("utf-8"))
    except IOError:
        header = "HTTP/1.1 404 Not Found\r\n"
        body = "<h1>The page you are requesting does not exist!</h1>"
        content = "{}\r\n{}".format(header, body)
        connectionSocket.send(content.encode("utf-8"))
    finally:
        connectionSocket.close()


