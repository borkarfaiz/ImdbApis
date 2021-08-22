from functools import wraps
from flask import g, request, redirect, url_for
from flask_jwt_extended import get_jwt_identity
from databases.helper import get_imdb_db

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        db = get_imdb_db()
        email = get_jwt_identity()
        is_admin = bool(
            db.users.find_one(
                {'email': email, "is_admin": True}, 
                {"is_admin": 1}
            )
        )
        if not is_admin:
            return "not authorize", 205
        return f(*args, **kwargs)
    return decorated_function


