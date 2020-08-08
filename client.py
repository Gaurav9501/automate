import socket
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port=9999
soc.connect((host,port))
while True:
    msg = soc.recv(1024)
    print(msg.decode('ascii'))
    
