#SISTEMA DE CRIAÇAO E LEITURA DO BANCO DE DADOS 
import sqlite3

banco = sqlite3.connect('config/.db/sql.db',check_same_thread=False)
cursor = banco.cursor()
sql = 'SELECT * FROM dados WHERE email = ? and senha = ?'

def create(e, s):
    cursor.execute("CREATE TABLE IF NOT EXISTS dados (id integer PRIMARY KEY AUTOINCREMENT, email text,  senha text) ")
    cursor.execute(f"INSERT INTO dados (email, senha) VALUES(?,?)", (e, s))
    banco.commit()
    
def read(e,s):
    for row in cursor.execute(sql, (e,s)):
        id = row[0]
        login = row[1]
        senha = row[2]
        return id ,login,  senha
    

if __name__ == "__main__":
    #create('loock', '123456')
    id, lg, snh = read('loock', '123456')
    print (snh)