#!/usr/bin/env python
import socket
from turtle import st

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    host = socket.gethostname()  # as both code is running on same pc
    port = 5002  # socket server port number
    soc.connect((host, port))
    message = int(input("Enter Number:"))
    soc.sendall(str(message).encode())
    data = soc.recv(1024).decode()

    if int(data) == 0:
        answer = "even"
    else:
        answer = "odd"

    print(" Received From Server", message, "is", answer)
