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
	return password_context.verify(form_password, hashed_password) # True or False
