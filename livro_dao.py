import sqlite3
from model.livro import Livro

class LivroDAO:
    def __init__(self, db_path):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)
    
    def create(self, livro):
        pass

    def read(self, livro_id):
        pass

    def update(self, livro):
        pass

    def delete(self, livro_id):
        pass