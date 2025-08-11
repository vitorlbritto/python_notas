from sistema_biblioteca import *

livro1 = Livro('Mitologia Nórdica', 'Oaks')
livro2 = Livro('Mitologia Grega', 'Joseph')
livro3 = Livro('Mitologia Egipicia', 'David F. Smith')
livro4 = Livro('Mitologia Chinesa', 'Funabashi')

usuario1 = Usuario('Rogerinho')
usuario2 = Usuario('Luciano')
usuario3 = Usuario('Ferreira')
usuario4 = Usuario('Rafael')

biblioteca = Biblioteca()

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)

usuario1.emprestar(livro1)
usuario3.emprestar(livro4)
usuario4.emprestar(livro2)

usuario3.devolver(livro4)

livro_encontrado = biblioteca.buscar_livro('Mitologia Chinesa')



