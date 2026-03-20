from http import HTTPStatus

from fastapi.testclient import TestClient

from async_project.app import app


def verificar_rota_que_retorna_html():
    client = TestClient(app)  # arrange

    response = client.get('/return_html')  # act

    assert response.status_code == HTTPStatus.OK
