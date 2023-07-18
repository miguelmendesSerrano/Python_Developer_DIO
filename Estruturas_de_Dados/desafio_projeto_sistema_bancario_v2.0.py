import textwrap

def menu():
    menu = """
    =======================================
            SISTEMA BANCÁRIO v2.0
    =======================================
    [1] DEPOSITAR
    [2] SACAR
    [3] EXTRATO
    [4] NOVA CONTA
    [5] LISTAR CONTA
    [6] NOVO USUÁRIO
    [0] SAIR
    ========================================
    ==> """
    return int(input(textwrap.dedent(menu)))


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


def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe usuário com esse CPF!')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, n° - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('Usuário criado com sucesso!')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('Usuário não encontrado! Processo de criação de conta encerrado.')


def listar_contas(contas):
    if not contas:
        print('\nNenhuma conta para listar!')
    else:
        for conta in contas:
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/c:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print('=' * 40)
            print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input('\nDigite o valor que deseja depositar: R$'))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input('\nDigite o valor que deseja sacar: R$'))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite,
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES
            )
            
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 5:
            listar_contas(contas)

        elif opcao == 6:
            criar_usuario(usuarios)

        elif opcao == 0:
            print('\nSaindo do sistema...Obrigado!')
            break

        else:
            print('\nOpção inválida! Por favor digite novamente uma opção válida.')

main()
