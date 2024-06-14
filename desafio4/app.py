from flask import Flask, render_template, request
import json
import mysql.connector

app = Flask (__name__)

def arm(nome, email, celular, assunto, descricao):
    con=mysql.connector.connect(host='localhost', user='juliasantiago', password='15022024', database='desafio4')
    cur = con.cursor()
    salva = 'INSERT INTO contato (nome, celular, email, assunto, descricao) VALUES (%s, %s, %s, %s, %s)'
    valores = (nome, celular, email, assunto, descricao)
    cur.execute (salva, valores)
    con.commit()
    cur.close()
    con.close()
    return True

def leitura(table, column):
    con=mysql.connector.connect(host='localhost', user='juliasantiago', password='15022024', database='desafio4')
    cur = con.cursor()
    ler = 'SELECT * FROM contato'
    return True 

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/quemsomos")
def quemsomos():
    return render_template('quemsomos.html')

@app.route("/contatos", methods=["POST","GET"])
def contatos():
    nome=request.form.get('nome')
    assunto=request.form.get('assunto')
    email=request.form.get('email')
    descricao=request.form.get('descricao')
    celular=request.form.get('celular')
    arm(nome, email, celular, assunto, descricao)
    return render_template('contatos.html')



@app.route("/cardapio")
def cardapio():
    pratos=json.load(open("./templates/pratos.json",encoding="UTF-8"))
    p=[]
    for prato in pratos:
        p.append(prato)
    return render_template('cardapio.html',pratos=pratos,p=p)


