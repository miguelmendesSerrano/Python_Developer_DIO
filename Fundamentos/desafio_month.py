''' 
    TODO Faça uma relação entre as possíveis entradas e os meses (em inglês).
    TODO Imprima o valor de cada chave em relação as entradas do programa.
'''

month = int(input('Digite um número inteiro de 1 a 12: '))

months_dict = {
  1 : "January", 2 : "Febrary", 3 : "March", 4 : "April", 5 : "May", 6 : "June",
  7 : "July", 8 : "August", 9 : "September", 10 : "October", 11 : "November", 12 : "December"
}

print(f"{months_dict[month]}")
