import pytest

from libpythonpro_wf import github_api
from unittest.mock import Mock


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars3.githubusercontent.com/u/402714?v=4'
    resp_mock.json.return_value = {
        'login': 'renzo', 'id': 402714,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonpro_wf.github_api.requests.get')
    get_mock.return_value = resp_mock
    github_api.requests.get = Mock(return_value=resp_mock)
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('renzo')
    assert avatar_url == url


def test_url_valida():
    url = github_api.buscar_avatar('wfoschiera')
    resposta = 'https://avatars2.githubusercontent.com/u/7304236?v=4'
    assert url == resposta
