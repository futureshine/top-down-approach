from socket import *
import time
server_name = '127.0.0.1'
server_port = 12000
# create udp socket to connect the server
client_socket = socket(AF_INET, SOCK_DGRAM)
# set timeout to be 1 second
client_socket.settimeout(1)
# read the input from user
# message = input("Input lowercase sentence: ")
message = "test"
for i in range(10):
    client_socket.sendto(message.encode('utf-8'), (server_name, server_port))
    try:
        start_time = time.time()
        modified_message, server_address = client_socket.recvfrom(2048)
        end_time = time.time()
        ttl_msg = "the ping to {} is {} ms".format(server_name, (end_time-start_time)*1000)
        print(ttl_msg)
    except timeout as e:
        error_msg = "the ping to {} is lost".format(server_name)
        print(error_msg)
client_socket.close()
