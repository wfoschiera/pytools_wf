from libpythonpro_wf.github_api import buscar_avatar


def test_url_valida():
    url = buscar_avatar('wfoschiera')
    resposta = 'https://avatars2.githubusercontent.com/u/7304236?v=4'
    assert  url == resposta
