def carregar_arquivo(caminho,contatos):
    try:
        with open(caminho, 'r') as arquivo:
            for linha in arquivo:
                nome, telefone, email = linha.strip().split(',')
                contatos.append({'nome': nome, 'telefone': telefone, 'email': email})
    except FileNotFoundError:
        pass  

def salvar_arquivo(caminho,contatos):
    with open ('lista_contatos.txt','w') as arquivo:
        for contato in contatos:
            linha = f'{contato["nome"]},{contato["telefone"]},{contato["email"]}\n'
            arquivo.write(linha)
