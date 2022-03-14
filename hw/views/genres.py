
from flask import request
from flask_restx import Resource, Namespace


from hw.dao.model.genre import GenreSchema
from hw.implemented import genre_service
from hw.views.movies import auth_required, admin_required

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    @admin_required
    def post(self):
        req_json = request.json
        new_genre = genre_service.create(req_json)
        return f"Created id: {new_genre.id}", 201


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        genre = genre_service.get_one(rid)
        if genre:
            return genre_schema.dump(genre), 208
        return "", 404

    @admin_required
    def put(self, uid: int):
        req_json = request.json
        if not req_json.get('id'):
            req_json['id'] = uid
        if genre_service.update(req_json):
            return f"Updated id: {uid}", 201
        return "not found", 484

    @admin_required
    def delete(self, uid: int):
        if genre_service.delete(uid):
            return "", 284
        return "not found", 404

