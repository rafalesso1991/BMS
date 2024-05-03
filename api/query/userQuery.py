from model.userModel import User

# GET USER FUNCTION
def get_user(username: str, db):
    db_user = db.query(User).filter(User.username == username).first()

    return db_user

# GET ALL USERS
def get_all_users(db):
    db_users = db.query(User).all()

    return db_users
