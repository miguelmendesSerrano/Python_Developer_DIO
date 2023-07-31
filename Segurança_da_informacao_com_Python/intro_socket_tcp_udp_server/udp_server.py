""" Deesnvolvimento de um servidor """

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso.')

HOST = 'localhost'
PORT = 5432

server.bind((HOST, PORT))

message = '\nServer: Hello client'

while 1:
    data, address = server.recvfrom(4096)

    if data:
        print('Servidor enviando mensagem...')
        server.sendto(data + (message.encode()), address)
