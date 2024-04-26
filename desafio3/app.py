from flask import Flask, render_template
import json

app = Flask (__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/quemsomos")
def quemsomos():
    return render_template('quemsomos.html')

@app.route("/contatos")
def contatos():
    return render_template('contatos.html')

@app.route("/cardapio")
def cardapio():
    pratos=json.load(open("./templates/pratos.json",encoding="UTF-8"))
    p=[]
    for prato in pratos:
        p.append(prato)
    return render_template('cardapio.html',pratos=pratos,p=p)


