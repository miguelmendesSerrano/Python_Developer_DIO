# criando menu
menu = """
==============================
     SISTEMA BANCÁRIO v1.0
==============================

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR

Escolha uma das opções: """

# variáveis do sistema
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: # verificando opções válidas e funcionalidades do sistema

    opcao = int(input(menu))

    if opcao == 1: # opção depositar

        while True: # verificando valores válidos para depósito

            deposito = float(input('\nValor que deseja depositar: R$'))

            if deposito <= 0:
                print('\nValor inválido para deposito')
            else:
                print(f'\nDeposito no valor de R${deposito:.2f} realizado com sucesso.')
                saldo += deposito
                extrato += f"Depósito no valor de R${deposito:>.2f}\n"
                break

    elif opcao == 2: # opção sacar

        while True: # verificando valores válidos para saque

            saque = float(input('\nValor que deseja sacar: R$'))

            if saque <= 0:
                print('\nValor de saque inválido!')
                
            else: # verificando condições válidas para saque
                if saque > saldo:
                    print('\nSaldo insuficiente!')
                else:
                    if saque > limite:
                        print('\nValor limite de saque excedido!')
                    elif numero_saques >= LIMITE_SAQUES:
                        print('\nLimite de saques diários excedido')
                    else:
                        print('\nContando cédulas...Retire seu dinheiro')
                        saldo -= saque
                        numero_saques += 1
                        extrato += f"Saque no valor de R${saque:>.2f}\n"
                break

    elif opcao == 3: # opção extrato

        print(f'{" EXTRATO ":=^30}\n{extrato}\nSaldo atual R${saldo:>.2f}')
        print("=" * 30)

    elif opcao == 4: # opçao sair do sistema

        print('\nSaindo do sistema...Obrigado!')
        break

    else:
        print('\nOpção inválida! Tente novamente.')
