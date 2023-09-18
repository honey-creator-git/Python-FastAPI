from sqlalchemy import Column, Integer, String
from database import Base

class Payment(Base):
    __tablename__ = "PaymentLogs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    description = Column(String(200), nullable=False)
    currency_type = Column(String(80))
    payment_type = Column(String(80))
    status = Column(String(80))
    created_at = Column(String(80))
    def __repr__(self):
        return 'PaymentLogModel(user_id=%s, amount=%s, description=%s, currency_type=%s, payment_type=%s, status=%s, created_at=%s)' % (self.user_id, self.amount, self.description, self.currency_type, self.payment_type, self.status, self.created_at)
    
