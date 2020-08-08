import socket

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
host = socket.gethostname()
port = 9999
soc.bind((host,port))
soc.listen(5)
clientsoc,addr = soc.accept()
while True:
    msg = input()
    if(msg=="bye"):
        break;
    clientsoc.send(msg.encode('ascii'))
    print("connected")
