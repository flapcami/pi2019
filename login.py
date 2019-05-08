from flask import Flask, render_template, request, redirect, session
from gasto import Gasto
from cliente import Cliente
app = Flask (__name__)

lista = [Gasto('Transporte', 'Fixo', 300),
         Gasto('Alimentação', 'Mutável', 100),
         Gasto('Mercado', 'Mutável', 350)]

lista_clientes = []

@app.route("/")
def iniciar():
    return render_template('inicio.html', gastos=lista)

@app.route("/excluir_gasto")
def excluir_gasto():
    count = None
    den = request.args.get('den')
    for g in lista:
        if g.den == den:
            count = lista.index(g)
            break
    if count is not None:
        lista.pop(count)
        return iniciar()

@app.route ("/form_login")
def form_login ():
   return render_template("form_login.html")

@app.route ("/login", methods = ["POST"])
def login():
    login = request.form ["login"]
    senha = request.form ["senha"]

    for c in lista_clientes:    
        if c.user == login and c.senha == senha:
                session["usuario"] = login
                return redirect ("/")
        else :
                return "login ou senha inválidos"

@app.route ("/logout")
def logout():
    session.pop ("usuario")
    return redirect("/")

@app.route("/form_cadastro_cliente")
def form_cadastrar_cliente():
    return render_template("form_cadastro.html")  

@app.route("/cadastrar_cliente", methods = ["POST"])
def cadastrar_cliente():
    nome = request.form ["nome"] 
    cpf = request.form ["cpf"] 
    email = request.form["email"] 
    user= request.form["user"]
    senha = request.form["senha"]
    lista_clientes.append(Cliente(nome, cpf, user, senha, email))
    session["usuario"] = user
    return redirect("/")

app.config["SECRET_KEY"] = "51726.0"
app.run(debug= True)
