from hw.dao.director import DirectorDAO
from hw.dao.genre import GenreDAO
from hw.dao.movie import MovieDAO
from dao.user import UserDAO
from hw.service.director import DirectorService
from hw.service.genre import GenreService
from hw.service.movie import MovieService
from service.user import UserService
from hw.setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(user_dao=user_dao)
