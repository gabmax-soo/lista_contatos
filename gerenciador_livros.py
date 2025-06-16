livros = []

def adicionar_livro(titulo,autor,genero,ano):
    livro = {
        'titulo': titulo,
        'autor': autor,
        'genero':genero,
        'ano': ano
    }
    livros.append(livro)
    return 'Livro adicionado com sucesso!!!'
def listar_livros():
    if len(livros) == 0:
        return 'Não há livros na aqui.'
    else:
        for livro in livros:
            print(f'Titulo: {livro['titulo']}')
            print(f'Autor: {livro['autor']}')
            print(f'Genero: {livro['genero']}')
            print(f'Ano: {livro['ano']}')
        return '----------------------------'
def remover_livro(titulo):
    for livro in livros:
        if livro['titulo'] == titulo:
            livros.remove(livro)
            return 'Livro removido com sucesso!!!'
    return 'Livro não encontrado.'
def buscar_livro(titulo):
    for livro in livros:
        if livro['titulo'] == titulo:
            return livro
    return 'Livro não encontrado'

while True:
    print('------Cadastro de Livros------')
    print('1.Adicionar livro:')
    print('2.Listar Livros:')
    print('3.Buscar Livro:')
    print('4.Remover Livro: ')
    print('5.Finalizar o Sistema: ')

    try:
        opcao = int(input('Digite a opção que você deseja: '))
        if opcao == 1:
            titulo = input('Digite o titulo do livro:')
            autor = input('Digite o nome do autor: ')
            genero = input('Digite o genero do livro: ')
            ano = int(input('Digite o ano de publicação: '))
            print(adicionar_livro(titulo,autor,genero,ano))
        elif opcao == 2:
            print('------Lista de livros-------')
            print(listar_livros())
        elif opcao == 3:
            buscar = input('Qual o livro que deseja achar? ')
            print(buscar_livro(buscar))
        elif opcao == 4:
            remover = input('Qual livro deseja remover? ')
            print(remover_livro(remover))
        elif opcao == 5:
            print('Sistema Finalizando.....')
            break
        else:
            print('Opcao Invalida!!!')
            continue
    
    except ValueError:
        print('Digite um numero inteiro como opção.')
    
    

