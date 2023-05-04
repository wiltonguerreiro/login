from time import sleep

usuarios = list()
senhas = list()

def registrar_usuario():
    cadastrado = 0
    while cadastrado == 0:
        user = input('Nome: ').upper().split()
        if user in usuarios:
            print('Usuário já existe.')
            while True:
                novamente = int(input('1 - Tentar novamente\n0 - Sair\nSua opção: '))
                if novamente == 0:
                    break
                elif novamente != 1:
                    print('Opção inválida.')
                else:
                    break
            sleep(1)
            break
        else:
            senha = input('Senha: ')
            if len(senha) < 6:
                print('Senha muito curta, insira até 6 caracteres.')
            else:
                usuarios.append(user)
                senhas.append(senha)
                cadastrado = 'Cadastradado com sucesso.'

        if cadastrado != 0:
            print(cadastrado)

    cadastrado = 0

def entrar_usuario():
    while True:
        nome = input('Nome: ').upper().split()
        senha = input('Senha: ')

        if nome in usuarios:

            encontrar_senha = usuarios.index(nome)

            if senha == senhas[encontrar_senha]:
                while True:
                    print(f'Bem-Vindo {usuarios[encontrar_senha]}!')
                    sair = float(input('Digite [0] para sair.\n'))
                    
                    if sair == 0:
                        break
                break
            else:
                print('Senha incorreta.')
        else:
            print('Usuário incorreto ou não cadastrado.')
            while True:
                novamente = int(input('1 - Tentar novamente\n0 - Sair\nSua opção: '))
                if novamente == 0:
                    break
                elif novamente != 0 and novamente != 1:
                    print('Opção inválida')
            sleep(1)            
