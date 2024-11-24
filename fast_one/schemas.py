from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class userSchema(BaseModel):
    username: str
    email: EmailStr
    passwrod: str


class userPublic(
    BaseModel
):  # retorna o nome de usuário e email, mas não a senha
    id: int
    username: str
    email: EmailStr


class userDB(userSchema):
    id: int
