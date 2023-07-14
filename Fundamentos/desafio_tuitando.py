''' 
    TODO Ler a variável de entrada e verificar se ela possui mais ou menos que 140 caracteres.
    Se for maior imprima "MUTE" e se for igual ou menor imprima "TWEET".
'''

text = input('Text: ')

total_caracteres = len(text)

if total_caracteres <= 140:
    print('TWEET')
else:
    print('MUTE')
