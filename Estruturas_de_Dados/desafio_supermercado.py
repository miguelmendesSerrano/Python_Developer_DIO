''' 
  TODO Ler as variáveis de entrada N e K. Talvez seja necessário fazer um "split" na linha 
  para obtenção dos valores.
  TODO Calcular e imprimir o número de garrafas que o cliente terá no segundo dia, se 
  aproveitar ao máximo a oferta.
'''
    
T = int(input())

for i in range(T):
    N, K = input().split()
    N = int(N)
    K = int(K)
    print(N//K + N%K)
