
from sqlalchemy.orm import Session
from repository import UserRepository
from schema import UserCreateRequest
from user import User



class UserService:

    def __init__(self):
        self.user_repository = UserRepository()
    

    def create_user(self, db: Session, user_payload: UserCreateRequest):
         user= User(name =  user_payload.name,
                               email= user_payload.email,
                               age= user_payload.age
                               )

         self.user_repository.create_user(db, user)

    def get_all_users(self,db:Session):
            return self.user_repository.get_all_user(db)

    def get_user_by_email(self, db:Session, email:str):
             return self.user_repository.get_user_by_email(db, email)

    def delete_by_email(self, db:Session,email:str):  
        self.user_repository.delete_by_email(db, email)
        return "Deleted successfully"
         

         



        