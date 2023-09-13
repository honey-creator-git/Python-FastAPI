from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import model, schema
import datetime

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class UserRepo:
    
    async def create(db: Session, user: schema.UserCreate):
        hashed_password = pwd_context.hash(user.password)
        created_at = datetime.datetime.now()
        created_year = str(created_at.year)
        created_month = str(created_at.month)
        created_day = str(created_at.day)
        db_user = model.User(email=user.email, full_name=user.full_name, password=hashed_password, created_at=created_year+"-"+created_month+"-"+created_day, subscription_expired=True, role=2)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    async def fetch_by_email(db: Session, email):
        return db.query(model.User).filter(model.User.email == email).first()