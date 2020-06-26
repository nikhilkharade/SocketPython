import socket
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 5001

server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)

server_socket.bind((IP , PORT))

server_socket.listen()

socket_list = [server_socket]

clients = {}

def recieve_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        
        message_length = int(message_header.decode("utf-8").strip())
        return {"header" : message_header , "data" : client_socket.recv(message_length)}
    
    except:
    	return False
   