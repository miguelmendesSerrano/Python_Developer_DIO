# Programa simples para disparar ping e verificar coneções
from os import system

print('-' * 60)
ip_host = input('Digite o HOST ou ip que deseja verificar: ')
print('-' * 60)
system(f'ping -n 2 {ip_host}')
print('-' * 60)
