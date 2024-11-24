from http import HTTPStatus

from fastapi import FastAPI

from fast_one.schemas import Message, userDB, userPublic, userSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)  # end point
def read_root():
    return {'message': 'busquem conhecimento'}


fakedb = []  # provisório para estudos


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=userPublic)
def createUser(user: userSchema):
    userWithID = userDB(
        id=len(fakedb) + 1,
        **user.model_dump(),  # cria um dicionário com os dados do pydentic
    )

    fakedb.append(userWithID)

    return userWithID
