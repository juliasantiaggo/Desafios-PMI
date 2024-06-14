import mysql.connector


def leitura():
    con=mysql.connector.connect(host='localhost', user='juliasantiago', password='15022024', database='desafio4')
    cur = con.cursor()
    ler = f'SELECT * FROM contato'
    cur.execute(ler)
    res = cur.fetchall()
    return res

print(leitura())