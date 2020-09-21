from libpythonpro.github_api import buscar_avatar


def test_url_valida():
    usuario = 'wfoschiera'
    resposta = 'https://avatars2.githubusercontent.com/u/7304236?v=4'
    assert buscar_avatar(usuario) == resposta
