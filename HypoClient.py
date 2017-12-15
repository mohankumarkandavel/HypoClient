import socket

HOST = "localhost"
PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def SockConnect():
    sock.connect((HOST, PORT))
    print("socket connected")
    return sock

def SockClose():
    sock.close()
    print("socket closed")

def SockSendAll(data):
    sock.sendall(data)
    '''print("send data:" + data.decode('utf-8'))'''

def SockReceive(socket):
    while True:
        data = socket.recv(1024)
        print("received data:" + data.decode('utf-8'))
        if not data:break
    return data

'''sock.sendall(b"Hello\n")
dataa = recv_basic(sock)

if(data == b'olleH\n'):
    sock.sendall(b"Bye\n")
    data = sock.recv(1024)
    print("2)", data)

    if(data == "eyB\n" ):
        sock.close()
        print("Socket closed")'''
