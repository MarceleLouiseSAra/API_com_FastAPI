from http import HTTPStatus


def test_read_root_deve_retornar_200_e_messagem(client):
    # client = TestClient(app)  # arrange

    response = client.get('/')  # act

    # assert response.status_code == 200
    # assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.status_code == HTTPStatus.OK  # deu certo a requisição?
    assert response.json() == {'message': 'busquem conhecimento'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'marcele',
            'email': 'marcele@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED  # retornou 201?
    assert response.json() == {
        'username': 'marcele',
        'email': 'marcele@example.com',
        'id': 1,
    }
