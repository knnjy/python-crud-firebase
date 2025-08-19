from pydantic import BaseModel, EmailStr
 
class UserResponseDTO(BaseModel):
    id: str
    username: str
    name: str
    email: EmailStr
    role: str
    is_active: bool