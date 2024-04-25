from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class User(Base):
    __tablename__ = 'user'

    id = Column("user_id", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    email = Column(String(40))

    data_insercao = Column(DateTime, default=datetime.now())

    favorites = relationship("Favorite", back_populates="user")

    def __init__(self, nome:str, 
                 email:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um usuário

        Arguments:
            nome: nome do usuário
            email: email do usuario
            data_insercao: data de quando o produto foi inserido à base
        """
        self.nome = nome
        self.email = email


        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
