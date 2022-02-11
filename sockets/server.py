# server.py
#!/usr/bin/python                           # This is server.py file

import socket                               # Import socket module

s = socket.socket()                         # Create a socket object
host = "0.0.0.0"                            # Get local machine name
port = 12345                                # Reserve a port for your service.
print(host)
s.bind((host, port))                        # Bind to the port

s.listen(5)                                 # Now wait for client connections.
print('Esperando conexão.')
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Conectado a ', addr)

    flag = True

    while flag:
        print('Aguardando mensagem')

        data = c.recv(1024)
        print('Mensagem recebida:', data.decode())

        if data.decode() == "SAIR":
            break
        
        x = input('Digite a resposta: ')
        c.send(x.encode())

        if x == "SAIR":
            c.send("SAIR".encode())
            flag = False

        print('Resposta enviada.')

    c.close()                                # Close the connection
    print('Conexão encerrada.')