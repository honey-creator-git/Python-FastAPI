from sqlalchemy.orm import Session
from . import model, schema
import datetime

class SentimentResult:
    
    async def create(db: Session, sentimentResult: schema.SentimentResult):
        
        db_sentiment_result = db.query(model.SentimentResult).filter(model.SentimentResult.keyword == sentimentResult['keyword']).first()
        
        if not db_sentiment_result:
            created_at = datetime.datetime.now()
            created_year = str(created_at.year)
            created_month = str(created_at.month)
            created_day = str(created_at.day)
            
            db_sentimentResult = model.SentimentResult(keyword=sentimentResult['keyword'], label=sentimentResult['label'], score=sentimentResult['score'], created_at=created_year+"-"+created_month+"-"+created_day)
            db.add(db_sentimentResult)
            db.commit()
            db.refresh(db_sentimentResult)
            
            return "Sentiment Result Item saved successfully!!!"
        
        setattr(db_sentiment_result, 'label', sentimentResult['label'])
        setattr(db_sentiment_result, 'score', sentimentResult['score'])
        
        updated_at = datetime.datetime.now()
        updated_year = str(updated_at.year)
        updated_month = str(updated_at.month)
        updated_day = str(updated_at.day)
        
        db_sentiment_result.updated_at = updated_year+"-"+updated_month+"-"+updated_day
        db.add(db_sentiment_result)
        db.commit()
        db.refresh(db_sentiment_result)
        
        return "Sentiment Result Item updated successfully!!!"
            