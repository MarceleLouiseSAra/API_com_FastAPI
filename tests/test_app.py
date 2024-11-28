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


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'marcele',
                'email': 'marcele@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': 'password',
            'username': 'testusername2',
            'email': 'marcele@example.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'testusername2',
        'email': 'marcele@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.json() == {'message': 'User deleted'}
