from flask_bcrypt import Bcrypt
from flask_restful import Resource, request
from databases.helper import get_imdb_db

from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required


bcrypt = Bcrypt()


class SignUp(Resource):
    def post(self):
        db = get_imdb_db()
        data = request.json
        email = data.get('email')
        password = data.get('password')
        is_admin = data.get('is_admin')
        if db.users.find_one({'email': email}):
            return "Users already exist", 409
        hash_password = bcrypt.generate_password_hash(password)
        db.users.insert_one({
            "email": email,
            "password": hash_password,
            "is_admin": is_admin
        })
        return "SingUp Successful", 201


class Token(Resource):
    def post(self):
        db = get_imdb_db()
        data = request.json
        email = data.get('email')
        password = data.get('password')
        hash_password = db.users.find_one({"email": email}, {"password": 1, "_id": 0})
        if not hash_password or not bcrypt.check_password_hash(hash_password.get('password'), password):
            return "Invalid Credentials", 401
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)
        return {"access_token": access_token, "refresh_token": refresh_token}, 200


class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return {"access_token": access_token}, 201
