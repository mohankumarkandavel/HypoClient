import socket

HOST = "localhost"
PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

def recv_basic(the_socket):
    while True:
        data = the_socket.recv(1024)
        print(data)
        if not data:break
    return data

sock.sendall(b"Hello\n")
dataa = recv_basic(sock)

if(data == b'olleH\n'):
    sock.sendall(b"Bye\n")
    data = sock.recv(1024)
    print("2)", data)

    if(data == "eyB\n" ):
        sock.close()
        print("Socket closed")
