import json

from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Hike, User, Favorite
from logger import logger
from schemas import *
from flask_cors import CORS


def load_hikes_data_to_db():
    # Load data from JSON
    with open('base-db/hikes.json') as f:
        data = json.load(f)
    hikes_data = data['hikesData']

    # Create a new session
    session = Session()

    # Iterate over hikes data and add each to the session
    for hike in hikes_data:
        hike_obj = Hike(
            title=hike['title'],
            continent=hike['continent'],
            country=hike['country'],
            description=hike['description'],
            site=hike['site'],
            imageUrl=hike['imageUrl'],
            difficulty=hike['difficulty'],
            duration=hike['duration'],
            distance=hike['distance'],
            elevation=hike['elevation'],
            rating=hike['rating'],
            explained=hike['explained'],
            lat=hike['lat'],
            lng=hike['lng']
        )
        session.add(hike_obj)

    # Commit the session to save the data
    session.commit()


# Call the function to load data into the database
load_hikes_data_to_db()

info = Info(title="Great Hikes", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
hike_tag = Tag(name="Hike", description="Adição, visualização e remoção de trilhas à base")
user_tag = Tag(name="User", description="Adição, visualização e remoção de usuários à base")
favorite_tag = Tag(name="Favorite", description="Adição, visualização e remoção de trilhas favoritas por usuário")



@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# METODOS PARA TRILHAS

@app.post('/hike', tags=[hike_tag],
          responses={"200": HikeViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_hike(form: HikeSchema):
    """Adiciona uma nova trilha à base de dados

    Retorna uma representação das trilhas e comentários associados.
    """
    hike = Hike(
        title=form.title,
        continent=form.continent,
        country=form.country,
        description=form.description,
        site=form.site,
        imageUrl=form.imageUrl,
        difficulty=form.difficulty,
        duration=form.duration,
        distance=form.distance,
        elevation=form.elevation,
        rating=form.rating,
        explained=form.explained,
        lat=form.lat,
        lng=form.lng)
    logger.debug(f"Adicionando trilha de nome: '{hike.title}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando trilha
        session.add(hike)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado trilha de nome: '{hike.title}'")
        return apresenta_hike(hike), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "trilha de mesmo nome já salva na base :/"
        logger.warning(f"Erro ao adicionar trilha'{hike.title}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar nova trilha :/"
        logger.warning(f"Erro ao adicionar trilha '{hike.title}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/hikes', tags=[hike_tag],
         responses={"200": ListagemHikesSchema, "404": ErrorSchema})
def get_hikes():
    """Faz a busca por todas as trilhas salvas

    Retorna uma representação da listagem de trilhas.
    """
    logger.debug(f"Coletando trilhas")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    hikes = session.query(Hike).all()

    if not hikes:
        # se não há trilhas cadastradas
        return {"trilhas": []}, 200
    else:
        logger.debug(f"%d trilhas econtradas" % len(hikes))
        # retorna a representação da trilha
        print(hikes)
        return apresenta_hikes(hikes), 200


@app.get('/hike', tags=[hike_tag],
         responses={"200": HikeViewSchema, "404": ErrorSchema})
def get_hike(query: HikeBuscaSchema):
    """Faz a busca por uma trilha a partir do id da trilha

    Retorna uma representação das trilhas salvas.
    """
    hike_id = query.id
    logger.debug(f"Coletando dados sobre a trilha #{hike_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    hike = session.query(Hike).filter(Hike.id == hike_id).first()

    if not hike:
        # se a cor não foi encontrada
        error_msg = "Trilha não encontrado na base :/"
        logger.warning(f"Erro ao buscar trilha '{hike_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Trilha econtrada: '{hike.title}'")
        # retorna a representação de trilha
        return apresenta_hike(hike), 200


@app.delete('/hike', tags=[hike_tag],
            responses={"200": HikeDelSchema, "404": ErrorSchema})
def del_hike(query: HikeBuscaSchema):
    """Deleta uma trilha a partir do nome da trilha informada

    Retorna uma mensagem de confirmação da remoção.
    """
    hike_title = unquote(unquote(query.title))
    print(hike_title)
    logger.debug(f"Deletando dados sobre a trilha #{hike_title}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Hike).filter(Hike.title == hike_title).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletada a trilha #{hike_title}")
        return {"mesage": "Trilha removida", "nome": hike_title}
    else:
        # se a cor não foi encontrada
        error_msg = "Trilha não encontrada na base :/"
        logger.warning(f"Erro ao deletar a trilha #'{hike_title}', {error_msg}")
        return {"mesage": error_msg}, 404


# METODOS PARA USUÁRIOS -----


@app.post('/user', tags=[user_tag],
          responses={"200": UserViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_user(form: UserSchema):
    """Adiciona um novo usuário à base de dados

    Retorna uma representação dos usuários e comentários associados.
    """
    user = User(
        nome=form.nome,
        email=form.email)
    logger.debug(f"Adicionando usuário de nome: '{user.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando user
        session.add(user)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado usuário de nome: '{user.nome}'")
        return apresenta_user(user), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Usuário de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar usuário'{user.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo usuário :/"
        logger.warning(f"Erro ao adicionar user '{user.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/users', tags=[user_tag],
         responses={"200": ListagemUsersSchema, "404": ErrorSchema})
def get_users():
    """Faz a busca por todas os usuários salvas

    Retorna uma representação da listagem dos usuários.
    """
    logger.debug(f"Coletando users")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    users = session.query(User).all()

    if not users:
        # se não há cores cadastradas
        return {"cores": []}, 200
    else:
        logger.debug(f"%d cores econtradas" % len(users))
        # retorna a representação da cor
        print(users)
        return apresenta_users(users), 200


@app.get('/user', tags=[user_tag],
         responses={"200": UserViewSchema, "404": ErrorSchema})
def get_user(query: UserBuscaSchema):
    """Faz a busca por uma user a partir do id da user

    Retorna uma representação das usuários salvas.
    """
    user_id = query.id
    logger.debug(f"Coletando dados sobre a user #{user_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    user = session.query(User).filter(User.id == user_id).first()

    if not user:
        # se a cor não foi encontrada
        error_msg = "User não encontrado na base :/"
        logger.warning(f"Erro ao buscar cor '{user_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"User econtrada: '{user.nome}'")
        # retorna a representação de user
        return apresenta_user(user), 200


@app.delete('/user', tags=[user_tag],
            responses={"200": UserDelSchema, "404": ErrorSchema})
def del_user(query: UserBuscaSchema):
    """Deleta uma user a partir do nome da user informada

    Retorna uma mensagem de confirmação da remoção.
    """
    user_nome = unquote(unquote(query.nome))
    print(user_nome)
    logger.debug(f"Deletando dados sobre a user #{user_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(User).filter(User.nome == user_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado o usuário #{user_nome}")
        return {"mesage": "User removida", "nome": user_nome}
    else:
        # se o usuário não foi encontrado
        error_msg = "Usuário não encontrado na base :/"
        logger.warning(f"Erro ao deletar o usuário #'{user_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    


# METODOS PARA FAVORITOS 


@app.post('/favorite', tags=[favorite_tag],
          responses={"200": {"description": "A trilha foi adicionada aos favoritos com sucesso"},
                     "409": {"description": "Conflito de dados"},
                     "400": {"description": "Requisição inválida"}})
def add_favorite(form: FavoriteBaseSchema):
    try:
        add_favorite(form.user_id, form.hike_id)
        return {"message": "Trilha adicionada aos favoritos com sucesso"}, 200
    except IntegrityError:
        return {"message": "Essa trilha já está nos favoritos"}, 409
    except Exception as e:
        return {"message": str(e)}, 400



@app.get('/favorites/<int:user_id>', tags=[favorite_tag],
         responses={"200": {"description": "Lista das trilhas favoritas do usuário"},
                    "404": {"description": "Usuário não encontrado"}})
def get_favorites(user_id: int):
    session = Session()
    user = session.query(User).get(user_id)
    if user is None:
        return {"message": "Usuário não encontrado"}, 404

    favorite_hikes = [favorite.hike for favorite in user.favorites]
    return {"favorite_hikes": [hike.to_dict() for hike in favorite_hikes]}, 200




@app.delete('/favorite', tags=[favorite_tag],
            responses={"200": {"description": "A trilha foi removida dos favoritos com sucesso"},
                       "404": {"description": "Trilha não encontrada nos favoritos"},
                       "400": {"description": "Requisição inválida"}})
def delete_favorite(form: FavoriteSchema):
    session = Session()
    favorite = session.query(Favorite).filter_by(user_id=form.user_id, hike_id=form.hike_id).first()
    if favorite is None:
        return {"message": "Essa trilha não está nos favoritos"}, 404

    session.delete(favorite)
    session.commit()
    return {"message": "Trilha removida dos favoritos com sucesso"}, 200

