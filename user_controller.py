from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schema import UserCreateRequest
from user import User
from database import get_db
from service import UserService

router = APIRouter(
    prefix= "/user",
)

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreateRequest, db:Session = Depends(get_db)):
    service = UserService()
    service.create_user(db, payload)

@router.get("/list")
def get_all_users(db:Session =Depends(get_db)):
    service = UserService()
    return service.get_all_users(db)

@router.get("/{email}")
def get_user_by_email(email:str, db:Session = Depends(get_db)):
    service = UserService()
    return service.get_user_by_email(db,email)

@router.delete("/{email}")
def delete_by_email(email:str, db:Session =Depends(get_db)):
 service= UserService()
 return service.delete_by_email(db,email)