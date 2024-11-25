from dao.livro_dao import LivroDAO

class LivroRepository:
    def __init__(self, db_path):
        self.livro_dao = LivroDAO(db_path)

    def adicionar_livro(self, livro):
        pass

    def listar_livros(self):
        pass

    def buscar_livro(self, id):
        pass
