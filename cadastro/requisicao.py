import json

import requests


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta:
            return resposta.text
    except Exception as error:
        print(f'Erro ao fazer requisição: {error}')


def parsing(texto_da_resposta):
    try:
        texto_depois_do_parsing = json.loads(texto_da_resposta)
        if texto_depois_do_parsing:
            return texto_depois_do_parsing
    except Exception as error:
        print(f'Erro ao fazer o parsing: {error}')
