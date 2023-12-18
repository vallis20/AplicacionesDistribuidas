import secrets

secret_key = secrets.token_hex(16)
print(secret_key)
class Config:
    DEBUG = True
    SECRET_KEY = secret_key
