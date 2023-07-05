from fastapi import APIRouter, Path, Query, Depends
from typing import List
from middelwares.jwt_middelware import JWTBearer
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from config.database import Session
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

#para autenticar al admin
#dependencies=[Depends(JWTBearer())]
@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return jsonable_encoder(result)


@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=200)
def filter_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content="Movie not found")
    return jsonable_encoder(result)    


@movie_router.get('/movies/', tags=['movies'], status_code=200)
#con query validamos queries
def get_movies_by_category(category: str = Query(min_length=4, max_length=15)) -> Movie:
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content="Category not found")
    return jsonable_encoder(result)   


@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    res = MovieService(db).create_movie(movie)
    return res


@movie_router.put('/movies/{id}', tags=['movies'], response_model=Movie, status_code=200)
def update_movie(id: int, movie: Movie) -> Movie:
    db = Session()
    result = MovieService(db).update_movie(id, movie)
    if not result:
        return JSONResponse(status_code=404, content="Movie not found")
    return result

    


@movie_router.delete('/movies/{id}', tags=['movies'], response_model=List[Movie], status_code=200)
def delete_movie(id: int):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    final = {}
    if not result:
        return JSONResponse(status_code=404, content="Movie not found")
    final = jsonable_encoder(result)
    db.delete(result)
    db.commit()
    return final



