from repository.livro_repository import LivroRepository

class LivroController:
    def __init__(self, db_path):
        self.livro_repo = LivroRepository(db_path)

    def adicionar_livro(self):
        pass

    def listar_livros(self):
        pass

    def editar_livro(self):
        pass

    def excluir_livro(self):
        pass
