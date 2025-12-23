import jwt, os, datetime
SECRET = os.getenv("JWT_SECRET")

def generate_token(tenant):
    return jwt.encode(
        {"tenant": tenant, "exp": datetime.datetime.utcnow()+datetime.timedelta(hours=12)},
        SECRET,
        algorithm="HS256"
    )

def verify_token(token):
    return jwt.decode(token, SECRET, algorithms=["HS256"])
