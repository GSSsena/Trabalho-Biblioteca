import sqlite3

def criar_tabela():
    try:
        conexao = sqlite3.connect("Biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,         
        ano  INTEGER,
        disponivel TEXT            
        )
        """)

    except Exception as erro:
        #Caso ocorra algum erro no banco
        print(f"erro ao tenta criar a tabela {erro}")
    finally:
        #Sempre fechar a conexão
        if conexao:
            conexao.close()
            


def cadrastrar_livro(titulo, autor, ano):
    try:
        conexao = sqlite3.connect("Biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO livros (titulo,autor,ano, disponivel)
        VALUES(?,?,?, ?)              
        """,
        (titulo,autor,ano, "sim")   
        )
        conexao.commit()
    except Exception as erro:
        #Caso ocorra algum erro no banco
        print(f"erro ao tenta criar a tabela {erro}")
    finally:
        #Sempre fechar a conexão
        if conexao:
            conexao.close()
    

titulo = input("Digite o titulo do livro:")
autor = input("Digite o nome do autor:")
ano = int(input("coloque o ano do livro:"))
cadrastrar_livro(titulo, autor, ano)



