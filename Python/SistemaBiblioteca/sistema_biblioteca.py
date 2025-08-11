class Livro:
    def __init__ (self, titulo, autor, disponivel=True ):
        # Inicializa o livro com título, autor e disponibilidade (padrão: disponível)
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def __str__(self):
        # Retorna uma string com o título e o autor do livro
        return f"{self.titulo} - {self.autor}"

class Usuario:
    def __init__ (self, nome):
        # Inicializa usuário com nome e lista vazia de livros emprestados
        self.nome = nome
        self.livros_emprestados = []

    def emprestar(self, livro):
        # Empresta o livro se estiver disponível, adicionando-o à lista e marcando como indisponível
        if livro.disponivel:
            self.livros_emprestados.append(livro)
            livro.disponivel = False
            return True
        else:
            print('LivroIndisponivelError')
    
    def devolver(self, livro):
         # Devolve o livro se estiver na lista de empréstimos, removendo-o e marcando como disponível
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.disponivel = True
        else:
            print("LivroNaoEmprestadoError")

class Biblioteca:
    def __init__ (self):
        # Inicializa a biblioteca com um catálogo vazio (lista de livros)
        self.catalogo = []

    def adicionar_livro(self, livro):
        # Adiciona um livro ao catálogo da biblioteca
        self.catalogo.append(livro)
    
    def buscar_livro(self, titulo):
        # Busca um livro pelo título no catálogo e retorna o objeto, ou None se não encontrado
        for livro in self.catalogo:
            if livro.titulo.lower == titulo:
                print(f'Livro {titulo} encontrado!')
                return livro
        print(f'Livro {titulo} não encontrado!')
        return None

        




        


