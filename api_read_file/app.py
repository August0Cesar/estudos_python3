import os
from openpyxl import load_workbook
from download_module import make_download
from map_json import busca_map_json


def create_folder(name_folder):
    
    if not os.path.exists(name_folder):
        os.makedirs(name_folder)

    

def busca_pergunta_id(checklist, pergunta):
    dic_perguntas = busca_map_json()

    if checklist in dic_perguntas.keys():
        
        for dic in dic_perguntas[checklist].items():
            if dic[1] == pergunta:
                return dic[0]
            
    return None

def valida_nome_arquivo():
    pass


def download_files(file):
    wb = load_workbook('Arquivos_2.xlsx') # abrindo o Workbook test.xlsx
    ws = wb['Sheet']
    
    cont = 0
    for line in ws: 
        if cont != 0:
            url_str = line[0].value.strip()
            file_name = line[1].value.strip()
            unidade = line[5].value.strip()
            checklist = line[6].value.strip()
            pergunta = line[7].value.strip() if line[7].value != None and line[7].value != '' else 'Valor em branco'
            data = f'{line[3].value.day}-{line[3].value.month}-{line[3].value.year}'
            id_pergunta = busca_pergunta_id(checklist,pergunta)
            dir_downlod = os.path.dirname(os.path.abspath(__file__)) + f'/files/{unidade}/{checklist}/{data}/{id_pergunta}/'
        
            create_folder(dir_downlod)
            make_download(dir_downlod, file_name, url_str)
            print(f'Imagem => {cont}')
            # break
        cont += 1

if __name__ == '__main__':
    # print(busca_pergunta_id('Visita Técnica V 1.0', 'Os letreiros não possuem nenhuma lâmpada queimada? Caso tenha, as lâmpdas do Menuboard não possuem nenhuma lâmpada queimada?'))
    download_files('Arquivos_2.xlsx')


