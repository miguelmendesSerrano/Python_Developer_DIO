
def menu():
    menu = """
=======================================
         SISTEMA BANCÁRIO v2.0
=======================================
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR
========================================
==> """

    return int(input(menu))


def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print('\nOperação falhou! Valor inválido para depósito.')
    else:
        saldo += valor
        extrato += f'Depósito no valor de \tR${valor:.2f}\n'
        print('\nDepósito realizado com sucesso!')

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor > saldo:
        print('\nOperação falhou! Saldo insuficiente.')

    elif valor > limite:
        print('\nOperação falhou! Valor limite por saque excedido.')

    elif numero_saques >= limite_saques:
        print('\nOperação falhou! Número de saques diários excedido.')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque no valor de \tR${valor:.2f}\n'
        numero_saques += 1
        print('\nContando cédulas...Retire seu dinheiro ==>')

    else:
        print('Operação falhou! Valor informado é inválido.')

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print(f'{" EXTRATO ":=^40}\n')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo atual R${saldo:.2f}')
    print('=' * 40)

def main():
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input('Digite o valor que deseja depositar: R$'))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input('Digite o valor que deseja sacar: R$'))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite,
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES)
            
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            break

        else:
            print('Opção inválida! Por favor digite novamente uma opção válida.')

main()
