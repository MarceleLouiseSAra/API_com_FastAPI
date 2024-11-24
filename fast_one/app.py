from http import HTTPStatus
from fastapi import FastAPI
from fast_one.schemas import Message, userSchema, userPublic

app = FastAPI()

@app.get('/')  # end point
def read_root():
    return {'message': 'busquem conhecimento'}

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)  # end point
def read_root():
    return {'message': 'busquem conhecimento'}

@app.post('/users/', response_model=userPublic)
def createUser(user : userSchema):
    return user