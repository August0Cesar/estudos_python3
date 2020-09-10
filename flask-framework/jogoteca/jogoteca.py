from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'augusto'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.__nome = nome
        self.__categoria = categoria
        self.__console =console
    
    @property
    def nome(self):
        return self.__nome

    @property
    def categoria(self):
        return self.__categoria

    @property
    def console(self):
        return self.__console

class Usuario:
    def __init__(self, id, nome, senha):
        self.__id = id
        self.__nome = nome
        self.__senha = senha
    
    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def senha(self):
        return self.__senha

usuario1 = Usuario('augusto', 'Augusto Cesar', '123456')
usuario2 = Usuario('ana', 'Ana Paula', '1a2')

dict_usuarios = {usuario1.id: usuario1, usuario2.id: usuario2 }        

jogo1 = Jogo('Gold of War 3', 'Ação', 'PS4')
jogo2 = Jogo('Hallo 4', 'Ação', 'XBOX One')
jogo3 = Jogo('Zeld LinkAwakness', 'RPG', 'Nintendo Swift')
lista_jogos = [jogo1, jogo2, jogo3]

@app.route('/jogos')
def rota_inicio():
    return render_template('jogos/lista.html', titulo ='Jogoteca',
                            jogos = lista_jogos)

@app.route('/jogos/novo')
def rota_novo_jogo():
    if not session['usuario_logado'] or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('rota_novo_jogo')))

    return render_template('jogos/novo.html', titulo ='Novo Jogo')  


@app.route('/jogos/criar', methods = ['POST'])
def rota_criar_jogo():
    novo_jogo = Jogo(request.form['nome'],
                    request.form['categoria'],
                    request.form['console'])

    lista_jogos.append(novo_jogo)

    return redirect(url_for('rota_inicio'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    return redirect(url_for('login'))   


@app.route('/autenticar', methods = ['POST',])
def autenticar():

    if request.form['usuario'] in dict_usuarios:
        usuario = dict_usuarios.get(request.form['usuario'])
        if(usuario.senha == request.form['senha']):
            session['usuario_logado'] = request.form['usuario']
            flash('Usuario {} logado com Sucesso'.format(usuario.nome))
            print(request.form['proxima_pagina'])
            return redirect(request.form['proxima_pagina'])
        
        flash('Usuario não encontrado')
        return redirect(url_for('login'))
    else:
        flash('Usuario não encontrado')
        return redirect(url_for('login'))


app.run(debug=True)