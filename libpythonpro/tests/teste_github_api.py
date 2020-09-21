from unittest import TestCase
from libpythonpro.github_api import buscar_avatar


class TesteGithubApi(TestCase):
    def teste_url_valida(self):
        usuario = 'wfoschiera'
        resposta = 'https://avatars2.githubusercontent.com/u/7304236?v=4'
        self.assertEqual(buscar_avatar(usuario), resposta)
