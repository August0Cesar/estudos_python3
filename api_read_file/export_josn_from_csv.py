import json
import csv
import random
from datetime import datetime
from br_nome_gen import pessoa_random

def escrever_json(lista):
    with open('file1600000.json', 'w') as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)
    print("finished!")

def create_date_timestamp():
    now = datetime.now()
    now = now.replace(day=random.randint(1, 31))
    return datetime.timestamp(now)


lista = []

# gera linhas
for cont in range(1, 1600001):
    pessoa = pessoa_random()
    nomes = pessoa.nome.split(" ")
    primeiro_nome = nomes[0]
    ultimo_nome = nomes[len(nomes) -1]
    email = f'{primeiro_nome}{ultimo_nome}@test.com'
    line = {}
    line['ID'] = cont
    line['Primeiro-Nome'] = primeiro_nome                         
    line['Ultimo-Nome'] = ultimo_nome
    line['Email'] = email.lower()
    line['Data-Cadastro'] = create_date_timestamp()
    line['Masculino'] = pessoa.masc
    lista.append(line)

print(f'Quanidade de objetos {len(lista)}')

# escreve arquivo
escrever_json(lista)
