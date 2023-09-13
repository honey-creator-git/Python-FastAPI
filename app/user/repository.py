from sqlalchemy.orm import Session
from . import model, schema

class UserRepo:
    
    async def create(db: Session, user: schema.UserCreate):
        db_user = model.User(email=user.email,full_name=user.full_name,password=user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    async def fetch_by_email(db: Session, email):
        return db.query(model.User).filter(model.User.email == email).first()