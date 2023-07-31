# Programa simples para disparar ping em varios HOST/ip para veficar conexão

from os import system
from time import sleep

with open('hosts.txt') as file:
    dump = file.read().splitlines()

    for ip in dump:
        print(f'Verificando o ip: {ip}')
        system(f'ping -n 2 {ip}')
        print('-' * 60)
        sleep(2)
