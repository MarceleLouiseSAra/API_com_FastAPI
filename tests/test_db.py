from sqlalchemy import select

from fast_one.models import User


def test_create_user(session):
    # engine = create_engine(
    #     'sqlite:///database.db'
    # )  # ponto de contato com o db

    user = User(
        username='sally',
        email='louise20marcele03@gmail.com',
        password='tch4birau',
    )

    session.add(user)
    session.commit()  # área de transferência

    result = session.scalar(
        select(User).where(User.email == 'louise20marcele03@gmail.com')
    )

    assert result.username == 'sally'
