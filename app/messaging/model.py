from sqlalchemy import Column, Integer, String
from database import Base

class Messaging(Base):
    __tablename__ = "Messaging"
    
    id = Column(Integer, primary_key=True, index=True)
    messaging = Column(String(300), nullable=False)
    created_at = Column(String(80))
    updated_at = Column(String(80))
    def __repr__(self):
        return 'Messaging(messaging=%s, created_at=%s, updated_at=%s)' % (self.messaging, self.created_at, self.updated_at)