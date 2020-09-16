from flask import Flask, render_template, request, redirect, session, flash, url_for,send_from_directory
from dao import JogoDao, UsuarioDao
from models import Usuario, Jogo
from helppers import recupera_imagem, deleta_arquivo
import time
import os
from jogoteca import app, db


dao_jogos = JogoDao(db)
dao_usuarios = UsuarioDao(db)

@app.route('/jogos')
def rota_inicio():
    lista_jogos = dao_jogos.listar()
    return render_template('jogos/lista.html', titulo ='Jogoteca',
                            jogos = lista_jogos)

@app.route('/jogos/editar/<int:id>')
def rota_editar_jogo(id):
    jogo = dao_jogos.busca_por_id(id)
    
    if not session['usuario_logado'] or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('rota_editar_jogo')))

    return render_template('jogos/edita.html', titulo='Editar Jogo', jogo=jogo,
                            capa_arquivo=recupera_imagem(id))  

@app.route('/jogos/salvar', methods = ['POST'])
def rota_salvar_jogo():
    novo_jogo = Jogo(request.form['nome'],
                    request.form['categoria'],
                    request.form['console'],
                    id=request.form['id'])

    
    jogo = dao_jogos.salvar(novo_jogo)
    arquivo = request.files['arquivo']

    deleta_arquivo(jogo.id)

    file_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    arquivo.save(f'{file_path}/capa_{jogo.id}_{timestamp}.jpg')
    return redirect(url_for('rota_inicio'))

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

    jogo = dao_jogos.salvar(novo_jogo)
    arquivo = request.files['arquivo']
    if arquivo:
        file_path = app.config['UPLOAD_PATH']
        timestamp = time.time()
        arquivo.save(f'{file_path}/capa_{jogo.id}_{timestamp}.jpg')
    return redirect(url_for('rota_inicio'))

@app.route('/imagem/<nome_arquivo>')
def imagem(nome_arquivo):
    if nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        return send_from_directory('uploads', nome_arquivo)
    return send_from_directory('uploads', 'imagem_padrao.jpg')

@app.route('/deletar/<int:id>')
def rota_deletar_jogo(id):
    dao_jogos.deletar(id)
    flash('Jogo deletado com sucesso')
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
    usuario =  dao_usuarios.buscar_por_id(request.form['usuario'])

    if usuario:
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