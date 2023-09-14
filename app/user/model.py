from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class User(Base):
    __tablename__ = "Users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(80), nullable=False, unique=True, index=True)
    full_name = Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)
    google_id = Column(String(80))
    updated_at = Column(String(80))
    created_at = Column(String(80))
    payment_verified = Column(Boolean)
    email_verified = Column(Boolean)
    subcription_at = Column(String(80))
    subscription_expired = Column(Integer)
    role = Column(Integer)
    def __repr__(self):
        return 'UserModel(email=%s, full_name=%s, password=%s, google_id=%s, updated_at=%s, created_at=%s, payment_verified=%s, email_verified=%s, subcription_at=%s, subscription_expired=%s, role=%s)' % (self.email, self.full_name, self.password, self.google_id, self.updated_at, self.created_at, self.payment_verified, self.email_verified, self.subcription_at, self.subscription_expired, self.role)
    