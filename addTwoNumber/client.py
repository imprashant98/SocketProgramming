#!/usr/bin/env python
import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5006  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    
    #numbers = list()

    #message = int(input("Enter numbers : "))  # take input

    while True:
        number1=input("enter the first number : ")
        if number1.lower().strip()=='exit':
            break
        number2=input("Enter the second number : ")
        
        
        message=number1+" "+number2;
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print(f'The summation of {number1} + {number2} = {data}')  # show in terminal
        

        #message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
