""" Desenvolvimento de um cliente TCP """

import socket
import sys


def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print('\nConexão falhou!')
        print(f'\nErro: {error}')
        sys.exit()

    print('\nSocket criado com sucesso.')

    host_target = input('Digite o HOST ou Ip a ser conectado: ')
    port_target = int(input('Digite a porta a ser conectada: '))

    try:
        client.connect((host_target, port_target))
        print(f'\nCliente TCP conectado com sucesso.\nHost: {host_target}\nPorta: {port_target}')
        client.shutdown(2)
    except socket.error as error:
        print(f'\nNão foi possível conectar no HOST: {host_target} porta: {port_target}')
        print(f'\nErro: {error}')
        sys.exit()


if __name__ == '__main__':
    main()
