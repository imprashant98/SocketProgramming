#!/usr/bin/env python
import socket

from turtle import st

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    host = socket.gethostname()  # as both code is running on same pc
    port = 5002  # socket server port number
    soc.bind((host, port))
    soc.listen(1)
    conn, addr = soc.accept()
    with conn:
        print("Accessed by: ", addr)
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            else:
                print("Number Inputted By client is", data)
                conn.sendall(str(int(data) % 2).encode())