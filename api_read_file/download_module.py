import io
import sys
import urllib.request as request
import requests

BUFF_SIZE = 1024

def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print('Downloaded {bytes}'.format(bytes=total_downloaded))

def download_length(response, output, length):
    times = length / BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(int(times)):
        output.write(response.read(BUFF_SIZE))
        print("Downloaded %d" % (((time * BUFF_SIZE)/length)*100))

def make_download(destino, file_name, url_str):

    with open(destino + file_name, 'wb') as imagem:
        resposta = requests.get(url_str, stream=True)

        if not resposta.ok:
            print("Ocorreu um erro, status:" , resposta.status_code)
        else:
            for dado in resposta.iter_content(1024):
                if not dado:
                    break

                imagem.write(dado)

            print("Imagem salva! =)")
