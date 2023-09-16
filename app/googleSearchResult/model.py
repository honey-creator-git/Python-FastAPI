from sqlalchemy import Column, Integer, String
from database import Base

class GoogleSearchResult(Base):
    __tablename__ = "GoogleSearchResults"
    
    id = Column(Integer, primary_key=True, index=True)
    search_id = Column(String(80), nullable=False)
    title = Column(String(80), nullable=False)
    link = Column(String(80), nullable=False)
    snippet = Column(String(200), nullable=False)
    created_at = Column(String(80))
    updated_at = Column(String(80))
    def __repr__(self):
        return 'GoogleSearchResults(search_id=%s, title=%s, link=%s, snippet=%s, created_at=%s, updated_at=%s)' % (self.search_id, self.title, self.link, self.snippet, self.created_at, self.updated_at)