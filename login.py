from time import sleep
from pack.bib import *

# Menu

while True:
    menu = int(input('''
----- MENU -----
1 - Cadastrar
2 - Entrar
0 - Sair

Opção: '''))

    if menu == 1:
        registrar_usuario()
        sleep(1)
        print('Retornando ao menu...')
        sleep(2)

    elif menu == 2:
        entrar_usuario()
        sleep(1)
        print('Retornando ao menu...')
        sleep(2)

    elif menu == 0:
        print('Até mais.')
        sleep(2)
        break

    else:
        print('Opção inválida.')
        sleep(2)
