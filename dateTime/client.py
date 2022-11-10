#!/usr/bin/env python
import socket
from datetime import datetime



def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5002  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

   # message = input(" -> ")  # take input
    date_today = datetime.now()
    message= date_today.strftime("%d/%m/%Y %H:%M:%S")
    print("client date and time for testing : "+message)
 
    client_socket.send(message.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response

    print('Received from server: ' + data)  # show in terminal
        
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
