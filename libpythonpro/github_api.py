import json

import requests


def buscar_avatar(usuario):
    """
    Busca a foto de perfil de um usuário no Github
    :param str com nome de um usuário no Github
    :return: str com a url da foto de perfil de um usuário no github
    """
    url = f'https://api.github.com/users/{usuario}'

    resp = requests.get(url)
    return resp.json()['avatar_url']