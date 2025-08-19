from app.utils.firebase_config import db
 
def db_collection(name: str):
    return db.collection(name)
 