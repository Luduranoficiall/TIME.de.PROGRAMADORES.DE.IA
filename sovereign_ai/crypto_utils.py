from cryptography.fernet import Fernet
import os

# Geração/recuperação de chave segura
FERNET_KEY = os.getenv("FERNET_KEY") or Fernet.generate_key().decode()
fernet = Fernet(FERNET_KEY.encode())

def encrypt(data: str) -> str:
    return fernet.encrypt(data.encode()).decode()

def decrypt(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()
