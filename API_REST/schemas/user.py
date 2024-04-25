from pydantic import BaseModel
from typing import Optional, List
from model.user import User

class UserSchema(BaseModel):
    """ Define como um novo usuário a ser inserido deve ser representado
    """
    nome: str 
    email: str 

class UserBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no email do usuario.
    """
    email: str = "yuricooke@gmail.com"
    id: int = 1
    

class ListagemUsersSchema(BaseModel):
    """ Define como uma listagem de usuários será retornada.
    """
    users:List[UserSchema]


def apresenta_users(users: List[User]):
    """ Retorna uma representação do usuário seguindo o schema definido em
        UserViewSchema.
    """
    result = []
    for user in users:
        result.append({
            "nome": user.nome,
            "email": user.email

        })

    return {"users": result}


class UserViewSchema(BaseModel):
    """ Define como um usuário será retornado: nome + e-mail.
    """
    id: int = 1
    nome: str = "Yuri Cooke"
    email: str = "yuricooke@gmail.com"


class UserDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_user(user: User):
    """ Retorna uma representação do usuário seguindo o schema definido em
        UserViewSchema.
    """
    return {
        "id": user.id,
        "nome": user.nome,
        "email": user.email
    }
