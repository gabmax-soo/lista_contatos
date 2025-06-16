contatos = []
while True:
    nome = input('Digite o nome do contato:')
    telefone = input('Digite o telefone do contato:')
    email = input('Digite o email do contato: ')

    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }
    
    contatos.append(contato)

    continuar = input('Deseja continuar? (s/n): ')
    if continuar != 's':
        break
print('------Lista de Contatos------')
for contato in contatos:
    print(f'Nome: {contato["nome"]}')
    print(f'Telefone: {contato["telefone"]}')
    print(f'Email: {contato["email"]}')
print('------------------------------')
