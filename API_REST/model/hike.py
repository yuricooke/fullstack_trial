from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base

class Hike(Base):
    __tablename__ = 'hike'

    id = Column("hike_id", Integer, primary_key=True)
    title = Column(String(140), unique=False)
    continent = Column(String(40), unique=False)
    country = Column(String(50), unique=False)
    description = Column(String(500), unique=False)
    site = Column(String(100), unique=False)
    imageUrl = Column(String(100), unique=False)
    difficulty = Column(Integer, unique=False)
    duration = Column(Integer, unique=False)
    distance = Column(Integer, unique=False)
    elevation = Column(Integer, unique=False)
    rating = Column(Integer, unique=False)
    explained = Column(String(2000), unique=False)
    lat = Column(Integer, unique=False)
    lng = Column(Integer, unique=False)
    data_insercao = Column(DateTime, default=datetime.now())

    favorites = relationship("Favorite", back_populates="hike")

    def __init__(self, title:str, continent:str, country:str, 
                 description:str, site:str, imageUrl:str, difficulty:int, 
                 duration:int, distance:int, elevation:int, rating:int, 
                 explained:str, lat:int, lng:int, 
                 data_insercao:Union[DateTime, None] = None):
        
        """
        Cria uma Trilha

        Arguments:
            Title: nome da trilha
            Continent: continente da trilha
            Country: país da trilha
            Description: descrição da trilha
            Site: site da trilha
            ImageUrl: url da imagem da trilha
            Difficulty: dificuldade da trilha
            Duration: duração da trilha
            Distance: distância da trilha
            Elevation: elevação da trilha
            Rating: avaliação da trilha
            Explained: explicação da trilha
            Lat: latitude da trilha
            Lng: longitude da trilha
            data_insercao: data de quando o produto foi inserido à base
        """

        self.title = title
        self.continent = continent
        self.country = country
        self.description = description
        self.site = site
        self.imageUrl = imageUrl
        self.difficulty = difficulty
        self.duration = duration
        self.distance = distance
        self.elevation = elevation
        self.rating = rating
        self.explained = explained
        self.lat = lat
        self.lng = lng

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
