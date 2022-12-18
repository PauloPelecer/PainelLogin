#SISTEMA DE EVENTOS PARA SER MOSTRADO NA TELA
import os
import re

def Reboot():
    os.system('python3 app.py')

def cls():
    os.system('clear')

def cursor(pg):
    c = input(str(f'\033[7;32m[\033[7;31m{pg}\033[7;32m]:\033[0;m'))
    return c
    
    
def pgmain():
    main = '''\033[0;33m
     [01]Login
     [02]Cadastrar
     \033[0;31m[00]Exit\033[0;m
    '''
    print (main)
    
def pglogin():
    msg = '''\033[0;33m
    Faça Login Na Nossa Plataforma Gratuitamente! Caso Não
    Tenha Uma Conta Crie Agora Mesmo Não Perca Tempo.
    Para Voltar Ao Inicio Digite \033[0;31m(Ctrl+c)\033[0;m
    '''
    print (msg)
    try:
        lg = cursor('Email')
        if len(lg) <= 7:
            cls()
            print ('Login Invalido')
            pglogin()
        else:
            s = cursor('Senha')
            if len(s) <= 4:
                cls()
                print ('Senha Invalida!')
                pglogin()
            else:
                return lg, s
    except:
        Reboot()       
        
         
def pgsingup():
    msg = '''\033[0;33m
    Faça Login Na Nossa Plataforma Gratuitamente! Caso Não
    Tenha Uma Conta Crie Agora Mesmo Não Perca Tempo.
    Para Voltar Ao Inicio Digite \033[0;31m(Ctrl+c)\033[0;m
    '''
    print (msg)
    try:
        lg = cursor('Email')
        if len(lg) <= 7:
            cls()
            print ('Email Invalido!')
            pgsingup()
        else:
            s = cursor('Senha')
            if len(s) <= 4:
                cls()
                print ('a senha com mais de 4 caracteres!')
                pgsingup()
            else:
                ss = cursor('Confirme a senha')
                if len(ss) <= 4:
                    cls()
                    print ('a senha com mais de 4 caracteres!')
                    pgsingup()
                elif ss == s:
                    return lg, ss
                else:
                    cls()
                    print ("Senha nao sao parecidas")
                    pgsingup()
    except:
        print ('exit...')
