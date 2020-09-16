import os
from jogoteca import app

def recupera_imagem(id):
    for nome_imagem in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa_{id}' in nome_imagem:
            return nome_imagem
    return 'imagem_padrao.jpg'

def deleta_arquivo(id):
    nome_arquivo = recupera_imagem(id)
    if not nome_arquivo == 'imagem_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'],nome_arquivo))