from sqlalchemy import Column, Integer, String
from database import Base

class InterventionRequest(Base):
    __tablename__ = "InterventionRequests"
    
    id = Column(Integer, primary_key=True, index=True)
    information = Column(String(200), nullable=False)
    additional_information = Column(String(200))
    created_at = Column(String(80))
    updated_at = Column(String(80))
    def __repr__(self):
        return 'InterventionRequests(information=%s, additional_information=%s, created_at=%s, updated_at=%s)' % (self.information, self.additional_information, self.created_at, self.updated_at)