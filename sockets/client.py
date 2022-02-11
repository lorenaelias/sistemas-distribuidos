# client.py

#!/usr/bin/python                      # This is client.py file

import socket                          # Import socket module

s = socket.socket()                    # Create a socket object
host = socket.gethostname()            # Get local machine name
port = 12345                           # Reserve a port for your service.

print('conectando-se ao servidor')
s.connect((host, port))
print('Conectado')

flag = True
while flag:

    x = input('Digite mensagem: ')
    s.send(x.encode())

    if(x == "SAIR"):
        break

    print('Mensagem enviada')

    print('Esperando resposta')
    data = s.recv(1024)
    print("Mensagem recebida: ", data.decode())

    if data.decode() == "SAIR":
        flag = False
        s.send("SAIR".encode())

print("Desconectando...")
s.close()                              # Close the socket when done
