from flask import Flask, render_template

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
    return render_template('cardapio.html')

@app.route("/eventos")
def eventos():
    return render_template('eventos.html')