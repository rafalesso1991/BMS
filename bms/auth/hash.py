from fastapi import HTTPException
from passlib.context import CryptContext
from schema.user_schema import UserResponse
#
ALGORITHM = "HS256"
# PASSWORD ENCRYPTER
password_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
# HASH GENERATOR FUNCTION
def generate_hash(plain_password):
	return password_context.hash(plain_password)
# PASSWORD VERIFIER FUNCTION
def verify_hashed_password(form_password, hashed_password):
	return password_context.verify(form_password, hashed_password)# True or False
# GET USER (BORRAR)
def get_user(db, username: str):
    if username in db: # si el 'username' está en la bbdd
        user_data = db[username]
        return UserResponse(**user_data) # devuelve un usuario rellenado con los datos de la bbdd
    return []
# GET USER (BORRAR)
def get_user(db, username: str):
    if username in db: # si el 'username' está en la bbdd
        user_data = db[username]
        return UserResponse(**user_data) # devuelve un usuario rellenado con los datos de la bbdd
    return []
# A LA CARPETA AUTH
def authenticate_user(db, username, password):
    user = get_user(db, username)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Authentication: User Not Found",
            headers={"WWW-Authenticate": "Bearer"}
        )
    if not verify_hashed_password(password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Authentication: Invalid Password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return user