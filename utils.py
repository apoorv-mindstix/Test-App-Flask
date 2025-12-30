from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import abort

def hash_password(password: str) -> str:
    return generate_password_hash(password)

def verify_password(hash_, password: str) -> bool:
    return check_password_hash(hash_, password)

def roles_required(*allowed_roles):
    """Decorator to restrict access based on roles in JWT claims."""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            role = claims.get('role')
            if role not in allowed_roles:
                abort(403, description='Forbidden')
            return fn(*args, **kwargs)
        return wrapper
    return decorator