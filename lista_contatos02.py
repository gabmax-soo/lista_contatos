contatos = []
def adicionar_contato(nome,telefone,email):
    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }
    contatos.append(contato)
    return 'Contato adicionado com sucesso'
def listar_contatos():
    for contato in contatos:
        print(f'Nome: {contato["nome"]}')
        print(f'Telefone: {contato["telefone"]}')
        print(f'Email: {contato["email"]}')
    return '-------------------------------'
    
def buscar(nome):
    for contato in contatos:
        if contato["nome"] == nome:
            return contato
    return 'Contato não encontrado'
def remover_contato(nome):
    for contato in contatos:
        if contato["nome"] == nome:
            contatos.remove(contato)
            return 'Contato removido com sucesso'
    return 'Esse contato não existe'

while True:
    print('1. Adicionar contato')
    print('2. Listar contatos')
    print('3. Buscar contato')
    print('4. Remover contato')
    print('5. Sair')
    
    opcao = int(input('Digite a opção desejada:'))

    if opcao == 1:
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone para contato: ')
        email = input('Digite o email do contato: ')
        print(adicionar_contato(nome,telefone,email))
    elif opcao == 2:
        print('------Lista de contatos-------')
        print(listar_contatos())
    elif opcao == 3:
        nome = input('Digite o nome do contato que deseja procurar:')
        print(buscar(nome))
    elif opcao == 4:
        nome = input('Digite o contato que deseja remover: ')
        print(remover_contato(nome))
    elif opcao == 5:
        print('Finalizando o programa...')
        break
    else:
        print('Opcao invalida!!!')
        continue

    