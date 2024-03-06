from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'])

def generate_hash(text):
	return password_context.hash(text)

def verify_hash(text, hash):
	return password_context.verify(text, hash)