from pydantic import BaseModel
from typing import Optional, List
from model.hike import Hike



class HikeSchema(BaseModel):
    """ Define como uma nova cor a ser inserida deve ser representada
    """
    id: int = 1
    title: str = "Yosemite National Park"
    continent: str = "North America"
    country: str = "United States"
    description: str = "Yosemite National Park is in California’s Sierra Nevada mountains. It’s famed for its giant, ancient sequoia trees, and for Tunnel View, the iconic vista of towering Bridalveil Fall and the granite cliffs of El Capitan and Half Dome."
    site: str = "https://www.nps.gov/yose/index.htm"
    imageUrl: str = "https://www.nps.gov/yose/planyourvisit/images/20170719_yose_001.jpg"
    difficulty: int = 3
    duration: int = 3
    distance: int = 10
    elevation: int = 1000
    rating: int = 5
    explained: str = "America's Yosemite National Park is a treasure trove of granite cliffs, waterfalls, and giant sequoias. Trails like the Mist Trail lead to iconic landmarks such as Yosemite Falls and Half Dome, offering hikers unparalleled views of the park's stunning landscapes."
    lat: int = 37.8651
    lng: int = -119.5383



class HikeBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da trilha.
    """
    
    id: int = 1
    title: str = "Yosemite National Park"
    continent: str = "North America"
    country: str = "United States"
    

class ListagemHikesSchema(BaseModel):
    """ Define como uma listagem de trilhas será retornada.
    """
    hikes:List[HikeSchema]


def apresenta_hikes(hikes: List[Hike]):
    """ Retorna uma representação da trilha seguindo o schema definido em
        HikeViewSchema.
    """
    result = []
    for hike in hikes:
        result.append({
            "id": hike.id,
            "title": hike.title,
            "continent": hike.continent,
            "country": hike.country,
            "description": hike.description,
            "site": hike.site,
            "imageUrl": hike.imageUrl,
            "difficulty": hike.difficulty,
            "duration": hike.duration,
            "distance": hike.distance,
            "elevation": hike.elevation,
            "rating": hike.rating,
            "explained": hike.explained,
            "lat": hike.lat,
            "lng": hike.lng
        })

    return {"hikes": result}


class HikeViewSchema(BaseModel):
    """ Define como uma trila será retornada: nome + title.
    """
    id: int = 1
    title: str = "Yosemite National Park"
    continent: str = "North America"
    country: str = "United States"


class HikeDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_hike(hike: Hike):
    """ Retorna uma representação da cor seguindo o schema definido em
        HikeViewSchema.
    """
    return {
        "id": hike.id,
        "title": hike.title,
        "continent": hike.continent,
        "country": hike.country

    }
