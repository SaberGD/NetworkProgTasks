#server broadcasting 
#Code by Mohamed Saber 

import threading
from socket import *

s=socket(AF_INET,SOCK_STREAM)
host = "127.0.0.1"
port = 8000
s.bind(host,port)
clients=[]
nicknames=[]

def broadcast(message,curr):
    for client in clients:
        if curr != client:
            client.send(message)

def handle (client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message,client)
        except:
            index=clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            broadcast(f'{nickname} has left'.encode('ascii'),client)
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client,addr=s.accept()
        print(f'server connected wit {addr[0]}')
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('asci')
        clients.append(client)
        nickname.append(nickname)
        print(f"{nickname} is nickname ")
        broadcast(f'{nickname} has joined'.encode('ascii'),client)
        client.send('connected to server !'.encode('ascii'))
        
        thread = threading.thread(target=handle , args=(client,))

receive()