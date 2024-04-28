from model.user_model import UserModel

# GET USER FUNCTION
def get_user(db, username: str):
    db_user = db.query(UserModel).filter(UserModel.username == username).first()
    return db_user

# GET ALL USERS
def get_all_users(db):
    db_users = db.query(UserModel).all()
    return db_users
