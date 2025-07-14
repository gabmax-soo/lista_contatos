from contatos import *
from arquivo import carregar_arquivo, salvar_arquivo

CAMINHO_ARQUIVO = 'lista_contatos.txt'

carregar_arquivo(CAMINHO_ARQUIVO,contatos)

def salvar():
    salvar_arquivo(CAMINHO_ARQUIVO,contatos)


while True:
    print('1. Adicionar contato')
    print('2. Listar contatos')
    print('3. Buscar contato')
    print('4. Remover contato')
    print('5. Sair')

    try:
        opcao = int(input('Digite a opção desejada:'))
    except ValueError:
        print('Digite um número valido.')
        continue


    if opcao == 1:
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone para contato: ')
        email = input('Digite o email do contato: ')
        print(adicionar_contato(nome,telefone,email,salvar))
    elif opcao == 2:
        print('------Lista de contatos-------')
        print(listar_contatos())
    elif opcao == 3:
        nome = input('Digite o nome do contato que deseja procurar:')
        print(buscar_contato(nome))
    elif opcao == 4:
        nome = input('Digite o contato que deseja remover: ')
        print(remover_contato(nome,salvar))
    elif opcao == 5:
        print('Finalizando o programa...')
        break
    else:
        print('Opção invalida!!!')
        continue
    


