class Livro:
    def __init__(self, id, titulo, isbn, data_publicacao, numero_paginas, autor_id, categoria_id):
        self.id = id
        self.titulo = titulo
        self.isbn = isbn
        self.data_publicacao = data_publicacao
        self.numero_paginas = numero_paginas
        self.autor_id = autor_id
        self.categoria_id = categoria_id
class Autores:
    def __init__(self, nome, titulo_do_livro, data_de_nascimento, nacionalidade, autor_id, genero_literario):
        self.nome = nome
        self.titulo = titulo_do_livro
        self.data_nascimento = data_de_nascimento
        self.nacionalidade = nacionalidade
        self.autor_id = autor_id
        self.genero_literario = genero_literario
