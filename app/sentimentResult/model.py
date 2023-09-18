from sqlalchemy import Column, Integer, String
from database import Base

class SentimentResult(Base):
    __tablename__ = "SentimentResults"
    
    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String(200), nullable=False)
    label = Column(String(80), nullable=False)
    score = Column(String(80), nullable=False)
    created_at = Column(String(80))
    updated_at = Column(String(80))
    def __repr__(self):
        return 'SentimentResults(keyword=%s, label=%s, score=%s, created_at=%s, updated_at=%s)' % (self.keyword, self.label, self.score, self.created_at, self.updated_at)