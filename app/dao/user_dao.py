from typing import Optional, List, Dict
from .utils_imports import db_collection
 
class UserDAO:
    COLLECTION = 'users'
 
    def __init__(self):
        self.col = db_collection(self.COLLECTION)

    def get_users(self) -> List[Dict]:
        docs = self.col.stream()
        out = []
        for d in docs:
            data = d.to_dict()
            data['id'] = d.id
            out.append(data)
        return out
    
    def create_user(self, data: dict) -> str:
        doc_ref = self.col.document()
        doc_ref.set(data)
        return doc_ref.id

 