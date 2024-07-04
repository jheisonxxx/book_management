import jwt
import datetime
from django.conf import settings

def generate_jwt(payload):
    return jwt.encode(
        {
            **payload,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
            'iat': datetime.datetime.utcnow(),
        },
        settings.JWT_SECRET,
        algorithm='HS256'
    )

def decode_jwt(token):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None