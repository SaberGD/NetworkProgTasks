#client broadcasting
#code by Mohamed Saber 

import threading
from socket import *

nickname= input("please enter your nickName: ")
client=socket(AF_INET,SOCK_STREAM)
host = "127.0.0.1"
port = 8000
client.connect(host,port)

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("an error occured! ")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input("")}"
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(Target = receive)
receive_thread.start()

write_thread = threading.thread(target=write)
write_thread.start()