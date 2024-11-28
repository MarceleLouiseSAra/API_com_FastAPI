from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_one.schemas import Message, userDB, userList, userPublic, userSchema

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


@app.get('/users/', response_model=userList)
def readUsers():
    return {'users': fakedb}


@app.put(
    '/users/{user_id}', response_model=userPublic
)  # user_id é uma variável
def update_user(user_id: int, user: userSchema):
    if user_id < 1 or user_id > len(fakedb):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='NOT FOUND',  # no coverage
        )

    userWithID = userDB(
        id=user_id,
        **user.model_dump(),  # cria um dicionário com os dados do pydentic
    )

    fakedb[user_id - 1] = userWithID

    return userWithID


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(fakedb):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found',  # no coverage
        )

    del fakedb[user_id - 1]

    return {'message': 'User deleted'}
