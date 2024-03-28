from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def generate_hash(plain_password):
	return password_context.hash(plain_password)

def verify_hash(plain_password, hashed_password):
	return password_context.verify(plain_password, hash)