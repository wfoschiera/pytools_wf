import requests


def buscar_avatar(usuario):
    """
    Busca o avatar do usuário no Github
    :param usuario: str com o nome do usuario
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    json = resp.json()
    return json['avatar_url']