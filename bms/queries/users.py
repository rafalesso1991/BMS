from model.user_model import UserModel

# OBTAIN USER FUNCTION
def obtain_user(db, username: str):
    db_user = db.query(UserModel).filter(UserModel.username == username).first()
    return db_user