""" Desenvolvimento de um cliente UDP """

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente: Socket criado com sucesso.')

HOST = 'localhost'
PORT = 5433
message = 'Hello server!'

try:
    print(f'Cliente: {message}')
    client.sendto(message.encode(), (HOST, 5432))

    data, server = client.recvfrom(4096)
    data = data.decode()
    print(f'Cliente: {data}')

finally:
    print('Cliente: Fechando conexão.')
    client.close()
