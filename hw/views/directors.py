from flask import request
from flask_restx import Resource, Namespace


from hw.dao.model.director import DirectorSchema
from hw.implemented import director_service
from hw.views.movies import auth_required, admin_required

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    @admin_required
    def post(self):
        req_json = request.json
        new_director = director_service.create(req_json)
        return f"Created id: {new_director.id}", 201


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid):
        director = director_service.get_one(rid)
        if director:
            return director_schema.dump(director), 200
        return "", 404

    @admin_required
    def put(self, uid: int):
        req_json = request.json
        if not req_json.get('id'):
            req_json['id'] = uid
        if director_service.update(req_json):
            return f"Updated id: {uid}", 201
        return "not found", 484

    @admin_required
    def delete(self, uid: int):
        if director_service.delete(uid):
            return "", 284
        return "not found", 404


