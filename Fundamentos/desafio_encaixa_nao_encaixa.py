n = int(input())  # primeiro número que entra é o '4' que é a quantidade de loops que deve ser feito

while n > 0:
    A, B = input().split()  # aqui onde o número será inserido e separados numa lista

    if (0 < len(A) <= 1000) and (0 < len(B ) <= 1000): #checaremos se o tamanho dos itens está dentro do permitido
        
        if A.endswith(B):       # iremos comparar se o final de A é igual o número B
            print('encaixa')
            
        else:
            print('nao encaixa')
    
    n -= 1
