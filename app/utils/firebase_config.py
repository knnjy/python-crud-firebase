import os
import firebase_admin 
from firebase_admin import credentials, firestore, auth
 
def init_firebase(app=None):
    # initialize firebase app once, using serviceAccountKey.json by default
    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "serviceAccountKey.json")
    if not firebase_admin._apps:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    # expose objects on module for convenience
    global db, firebase_auth
    db = firestore.client()
    firebase_auth = auth