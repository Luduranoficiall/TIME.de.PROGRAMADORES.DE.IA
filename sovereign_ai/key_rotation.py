import os
import secrets

def rotate_key(env_var: str = "FERNET_KEY"):
    new_key = secrets.token_urlsafe(32)
    # Exemplo: salvar em vault ou atualizar variável de ambiente
    os.environ[env_var] = new_key
    return new_key
