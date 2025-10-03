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
         print(f"erro ao tentar criar a tabela {erro}")
    finally:
         #Sempre fechar a conexão
         if conexao:
             conexao.close()
            


# def cadrastrar_livro(titulo, autor, ano):
#     try:
#         conexao = sqlite3.connect("Biblioteca.db")
#         cursor = conexao.cursor()

#         cursor.execute("""
#         INSERT INTO livros (titulo,autor,ano, disponivel)
#         VALUES(?,?,?, ?)              
#         """,
#         (titulo,autor,ano, "sim")   
#         )
#         conexao.commit()
#     except Exception as erro:
#           #Caso ocorra algum erro no banco
#           print(f"erro ao tentar criar a tabela {erro}")#
#     finally:
#           #Sempre fechar a conexão
#         if conexao:
#             conexao.close()
    

# titulo = input("Digite o titulo do livro:")
# autor = input("Digite o nome do autor:")
# ano = int(input("coloque o ano do livro:"))
# cadrastrar_livro(titulo, autor, ano)


# def lista_livros():
#     try:
#         conexao = sqlite3.connect("Biblioteca.db")
#         cursor = conexao.cursor()

#         cursor.execute("SELECT * FROM livros")
#         for linha in cursor.fetchall():
#             print(f"ID: {linha[0]} | TITULO: {linha[1]} | AUTOR: {linha[2]} | ANO: {linha[3]}")
#             print("-"*50)
              
#     except Exception as erro:
#          #Caso ocorra algum erro no banco
#          print(f"erro ao tentar criar a tabela {erro}")
#     finally:
#          #Sempre fechar a conexão
#         if conexao:
#             conexao.close()

# lista_livros()            

# def Atualizar_Disponibilidade(id_livros):
#     try:
#         conexao = sqlite3.connect("Biblioteca.db")
#         cursor = conexao.cursor()

#         cursor.execute("SELECT disponivel FROM livros WHERE id = "(id_livros))
#         resultado = cursor.fetchall()
#         if resultado[0] == "sim":
#              novo_status = "nao"
#         else:
#              novo_status = "sim"
#         cursor.execute("UPDATE livros SET disponivel = ? WHERE id ?" , (novo_status,id_livros))
#         conexao.commit()
#     except Exception as erro:
#           #Caso ocorra algum erro no banco
#           print(f"ocoreu um erro {erro}")#
#     finally:
#           #Sempre fechar a conexão
#         if conexao:
#             conexao.close()

# livro_id =input("Digite o ID do livro que deseja atualizar: ")
# Atualizar_Disponibilidade(livro_id)         

def remover_Livro(id_livros):
    try:
        conexao = sqlite3.connect("Biblioteca.db")
        cursor = conexao.cursor

        cursor.execute("DELETE FROM livros WHERE id = ?", {id_livros})

        conexao.commit()

        if cursor.rewcount > 0:
            print("livro foi removido da tabela")
        else:
            print("Nenhum aluno ancotrado com o ID fornecido.")
    except Exception as erro:
         #Caso ocorra algum erro no banco
        print(f"erro ao tentar remover livro{erro}")
    finally:
         #Sempre fechar a conexão
        if conexao:
            conexao.close()

deletar = int(input("Digite o ID do livro que deseja deletar: "))
remover_Livro(deletar)            

       


          

        






