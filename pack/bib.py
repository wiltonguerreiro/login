from time import sleep

usuarios = list()
senhas = list()

def salvar_arquivos():
    with open("usuarios.txt", "a+") as arquivo_usuarios:
        arquivo_usuarios.seek(0) #função para colocar o cursor (o ponto de referencia) no começo do arquivo
        conteudo = arquivo_usuarios.read() #comando para ler o que está dentro do arquivo onde salvamos os usuarios e senhas.

        if not conteudo: #caso o arquivo esteja vazio
            arquivo_usuarios.write("Usuário;Senha\n") #abre arquivo novo e escreve no começo dele
        
        usuarios_str = [' '.join(user) for user in usuarios] #convertendo lista de lista em lista de str

        
        for usuario in usuarios_str:
            if usuario not in conteudo: #verifica se ja existe para evitar duplicação
                arquivo_usuarios.write(usuario + ';' + senhas[usuarios_str.index(usuario)])
                arquivo_usuarios.write('\n')

def ler_arquivos():
    arquivo_usuario = open("usuarios.txt", "r")
    for linha in arquivo_usuario:
        user_senha = linha.split(';')
        print("usuario é", user_senha[0])
        print("senha é", user_senha[1])


def registrar_usuario():
    cadastrado = 0
    while cadastrado == 0:
        user = input('Nome: ').upper().split()
        if user in usuarios:
            print('Usuário já existe.')
            while True:
                novamente = int(input('1 - Tentar novamente\n0 - Sair\nOpção: '))
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
                salvar_arquivos() #chama a função para salvar o usuário em arquivo txt

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
                novamente = int(input('1 - Tentar novamente\n0 - Sair\nOpção: '))
                if novamente == 0:
                    break
                elif novamente != 0 and novamente != 1:
                    print('Opção inválida')
            sleep(1)            
