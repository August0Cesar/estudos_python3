from flask import Flask, render_template, request

app = Flask(__name__)


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

jogo1 = Jogo('Gold of War 3', 'Ação', 'PS4')
jogo2 = Jogo('Hallo 4', 'Ação', 'XBOX One')
jogo3 = Jogo('Zeld LinkAwakness', 'RPG', 'Nintendo Swift')
lista_jogos = [jogo1, jogo2, jogo3]

@app.route('/jogos')
def rota_inicio():
    
    return render_template('lista.html', titulo ='Jogoteca',
                            jogos = lista_jogos)

@app.route('/jogos/novo')
def rota_novo_jogo():
    return render_template('novo.html', titulo ='Novo Jogo')  


@app.route('/jogos/criar', methods = ['POST'])
def rota_criar_jog():
    print(request)

    novo_jogo = Jogo(request.form['nome'],
                    request.form['categoria'],
                    request.form['console'])

    lista_jogos.append(novo_jogo)

    return render_template('lista.html', titulo ='Jogoteca',
                            jogos = lista_jogos) 


app.run(debug=True)