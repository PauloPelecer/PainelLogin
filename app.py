#FERRAMENTA DE LOGIN - SIMULANDO ACESSO AO BANCO DE DADOS
from include import DataBase
from config import System

def configdb():
    try:
        id, lg, s = DataBase.read(user, password)
        System.cls()
        print ('Logado Com Sucesso!')
    except:
        System.cls()
        print ('Email ou Senha Incorreta ')

def createdb(e,s):
    try:
        em, sh = DataBase.read(e,s)
        if em == None:
            DataBase.create(e,s)
            print ("Conta Criada Com Sucesso!")
        else:
            print ('Esta Conta Ja Existe!')    
    except:
        DataBase.create(e,s)
        print ('Conta Criada!')
if __name__ == '__main__':
    System.cls()
    System.pgmain()
    try:
        c = System.cursor('Inicio')
        if c == '01' or c == '1':
            System.cls()
            user, password = System.pglogin()
            configdb()
        elif c == '02' or c == '2':
            System.cls()
            lg , s = System.pgsingup()
            createdb(lg,s)
        else:
            print ('exit...')
            
    except:
         System.Reboot()
