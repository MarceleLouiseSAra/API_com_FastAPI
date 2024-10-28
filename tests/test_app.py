from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_one.app import app

client = TestClient(app)


def test_read_root_deve_retornar_200_e_messagem():
    client = TestClient(app)  # arrange

    response = client.get('/')  # act

    # assert response.status_code == 200
    # assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.status_code == HTTPStatus.OK  # deu certo a requisição?
    assert response.json() == {'message': 'busquem conhecimento'}
