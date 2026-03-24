from http import HTTPStatus

from fastapi.testclient import TestClient

from async_project.app import app


# no pytest todo arquivo || função tem que comecar com test
def test_verificar_primeira_rota_hello_world():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK


def test_verificar_rota_de_html():
    client = TestClient(app)  # organizar

    response = client.get('/html_response')

    assert response.status_code == HTTPStatus.OK
    