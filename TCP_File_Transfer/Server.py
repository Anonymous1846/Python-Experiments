#our Objective is send files sockets 
#they provide end to end file transfer 
import socket
import os
#provide beautiful text art 
import pyfiglet
import random
#to serialize and the deserialize python objects !
import pickle
server_heading=pyfiglet.figlet_format(text='File Tranfer Server.')
print(server_heading)
#initializing the socket object !
server_socket=socket.socket()
PORT=43599
HOST=''
print(f'Binding the IP to the Port {PORT}')
server_socket.bind((HOST,PORT))
print('Now the server can listen upto 5 Clients Without Network Timeout !')
server_socket.listen(5)
conn,addr=server_socket.accept()
print(f'Now we\'re connected to {addr[0]}, which is on Port {addr[1]}')
with open('Hello.txt','rb') as f:
    some_text=f.read()
image_data=pickle.dumps(some_text)
size=os.path.getsize('Hello.txt')
conn.send(str(size).encode())
conn.send(image_data)
print(image_data)