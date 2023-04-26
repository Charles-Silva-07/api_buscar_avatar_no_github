import requests


def buscar_avatar(usuario):
    """
     Busca o avatar de um usuário no Github
    :param usuário: str com o nome de usuário no github
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('Charles-Silva-07'))