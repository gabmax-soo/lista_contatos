contatos = []

def adicionar_contato(nome, telefone, email, salvar_callback):
    contato = {'nome': nome, 'telefone': telefone, 'email': email}
    contatos.append(contato)
    salvar_callback()
    return 'Contato adicionado com sucesso'

def listar_contatos():
    if not contatos:
        return 'Nenhum contato cadastrado.'

    lista = ''
    for contato in contatos:
        lista += (
            f'Nome: {contato["nome"]}\n'
            f'Telefone: {contato["telefone"]}\n'
            f'Email: {contato["email"]}\n'
            f'-------------------------------\n'
        )
    return lista

def buscar_contato(nome):
    for contato in contatos:
        if nome in contato["nome"]:
            return (
                f'Nome: {contato["nome"]}\n'
                f'Telefone: {contato["telefone"]}\n'
                f'Email: {contato["email"]}')
    return 'Contato não encontrado'

def remover_contato(nome, salvar_callback):
    for contato in contatos:
        if contato["nome"] == nome:
            contatos.remove(contato)
            salvar_callback()
            return 'Contato removido com sucesso'
    return 'Esse contato não existe'


