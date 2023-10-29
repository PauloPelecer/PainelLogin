from flask import Flask, render_template, request, redirect
from include import database as db
from pathlib import Path
import re

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html',error='')
  else:
    Email = request.form['email']
    Pass = request.form['pass']
    textHtml = ''
    
    if len(Email)<= 3:
      textHtml = "Email Invalido!"
      
    if len(Pass) <=3:
      textHtml = 'Senha Invalida!'
    if len(Email) <=3 and len(Pass) <=3:
      textHtml= 'Preencha os Campos Acima!'
    try:
      global name
      id, name, email, senha = db.read(Email,Pass)
      return redirect('/home')
    except:
      
      return render_template('index.html',error=textHtml)
    
@app.route('/register', methods=['GET','POST'])
def register():
  if request.method == 'GET':
    return render_template('register.html')
  else:
    name = request.form['nome']
    email = request.form['email']
    emailVerifc = re.findall(r'.*@gmail\.com',email)
    password = request.form['pass']
    errorHtml = ''
    
    if len(name) <= 4:
      errorHtml= 'Nome Precisa Ter Mais de 4 Caracteres'
      return render_template('register.html',nameError=errorHtml)
    if len(email) <= 8:
      errorHtml = 'Email Invalido'
      return render_template('register.html',emailError=errorHtml)
    if emailVerifc == []:
      errorHtml = 'Email Invalido'
      return render_template('register.html',emailError=errorHtml)
    if len(password) <= 6:
      errorHtml = "A Senha Precisa Ter Mais de 6 Caracteres"
      return render_template('register.html',passwordError=errorHtml)
    else:
      try:
        id, name, email, senha = db.read(email,password)
        errorHtml = 'Essa Conta Ja Foi Criada'
        return render_template('register.html',passwordError=errorHtml)
      except:
        db.create(name,email,password)
        return redirect('/')
@app.route('/home',methods=['GET','POST'])
def home():
  if request.method == 'GET':
    return render_template('home.html', nameUser=name)
  else:
    return render_template('home.html',nameUser=name)
app.run(debug=True)