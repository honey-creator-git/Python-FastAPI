from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import model, schema
import datetime

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

class UserRepo:
    
    async def create(db: Session, user: schema.UserCreate):
        hashed_password = get_password_hash(user.password)
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
    
    async def fetch_by_email_password(db: Session, email, password):
        user = db.query(model.User).filter(model.User.email == email).first()
        if not user:
            return "User not exist"
        if not verify_password(password, user.password):
            return "Password is not correct"
        return user
    
    async def update_user_by_id(db: Session, user: schema.UserUpdate, id: int):
        db_user = db.query(model.User).filter(model.User.id == id).first()
        if not db_user:
            return "User not exist to update"
        
        # Update Model Class Variable from requestedd fields
        for var, value in vars(user).items():
            if (var == "password"):
                hashed_updated_pass = get_password_hash(value)
                setattr(db_user, var, hashed_updated_pass)
            if not (var == "password"):
                setattr(db_user, var, value) if value else None
            
        updated_at = datetime.datetime.now()
        updated_year = str(updated_at.year)
        updated_month = str(updated_at.month)
        updated_day = str(updated_at.day)
        
        db_user.updated_at = updated_year+"-"+updated_month+"-"+updated_day
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user