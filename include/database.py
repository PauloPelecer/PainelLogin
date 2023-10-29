#SISTEMA DE CRIAÇAO E LEITURA DO BANCO DE DADOS 
import sqlite3

banco = sqlite3.connect('static/sql.db',check_same_thread=False)
cursor = banco.cursor()
sql = 'SELECT * FROM dados WHERE email = ? and senha = ?'

def create(n ,e, s):
    cursor.execute("CREATE TABLE IF NOT EXISTS dados (id integer PRIMARY KEY AUTOINCREMENT,name text, email text,  senha text) ")
    cursor.execute(f"INSERT INTO dados (name ,email, senha) VALUES(?,?,?)", (n,e, s))
    banco.commit()
    
def read(e,s):
    for row in cursor.execute(sql, (e,s)):
        id = row[0]
        name = row[1]
        login = row[2]
        senha = row[3]
        return id, name,login,  senha
    

if __name__ == "__main__":
  pass
    #create('loock', '123456')
    #id, lg, snh = read('loock', '123456')
    #print (snh)