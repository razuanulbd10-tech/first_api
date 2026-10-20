from pydantic import BaseModel


class BaseUser(BaseModel):
     name:str
     email:str
     age: int 

class UserCreateRequest(BaseUser):
    pass

class UserResponse(BaseUser):
    id: int

    class Config:

        from_attribute = True 
    