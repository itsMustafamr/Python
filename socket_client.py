import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

while True:
    data = sock.recv(512) # can receive upto 512 charecters and get that back.
    if len(data) < 1:
        break
    print(data.decode(), end='') # decode basically does the opposite of encode above ie unicode to python readable string

sock.close()
