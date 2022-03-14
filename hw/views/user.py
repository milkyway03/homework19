from flask import request
from flask_restx import Namespace, Resource, reqparse
from marshmallow import Schema, fields
from hw.dao.model.user import UserSchema
from hw.implemented import user_service


user_ns = Namespace('users')
user_schema = UserSchema()
users_schema = UserSchema(many=True)
parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser. add_argument('role', type=str)


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()


@user_ns.route('/')
class UsersView(Resource):
    @user_ns.expect(parser)
    def get(self):
        req_args = parser.parse_args()
        if any(req_args.values()):
            all_users = user_service.get_filter(req_args)
        else:
            all_users = user_service.get_all()
        if all_users:
            return users_schema.dump(all_users), 200
        return "not found", 404

    def post(self):
        req_json = request.json
        new_user = user_service.create(req_json)
        return f"Created id: {new_user.id} Это новый пользователь!", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid: int):
        user = user_service.get_one(uid)
        if user:
            return users_schema.dump(user), 200
        return "", 404

    def put(self, uid: int):
        req_json = request.json
        if not req_json.get('id'):
            req_json['id'] = uid
        if user_service.update(req_json):
            return f"Updated id: {uid}", 201
        return "not found", 404

    def delete(self, uid: int):
        if user_service.delete(uid):
            return "", 204
        return "not found", 404
