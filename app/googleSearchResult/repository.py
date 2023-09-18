from sqlalchemy.orm import Session
from . import model, schema
import datetime

class GoogleSearchResult:
    
    async def create(db: Session, googleSearchResult: schema.GoogleSearchResult):
        
        db_google_search_result = db.query(model.GoogleSearchResult).filter(model.GoogleSearchResult.snippet == googleSearchResult['snippet']).first()
        
        if not db_google_search_result:
            created_at = datetime.datetime.now()
            created_year = str(created_at.year)
            created_month = str(created_at.month)
            created_day = str(created_at.day)
            
            hour = created_at.hour
            if(hour < 10):
                created_hr = str("0"+hour)
            created_hr = str(hour)
            minutes = created_at.minute
            if(minutes < 10):
                created_min = str("0"+minutes)
            created_min = str(minutes)
            
            db_googleSearchResult = model.GoogleSearchResult(search_id=googleSearchResult['search_id'], title=googleSearchResult['title'], link=googleSearchResult['link'], snippet=googleSearchResult['snippet'], created_at=created_year+"-"+created_month+"-"+created_day+" "+created_hr+":"+created_min)
            db.add(db_googleSearchResult)
            db.commit()
            db.refresh(db_googleSearchResult)
            
            return "Google Search Result item saved successfully!"
        
        setattr(db_google_search_result, 'search_id', googleSearchResult['search_id'])
        setattr(db_google_search_result, 'title', googleSearchResult['title'])
        setattr(db_google_search_result, 'link', googleSearchResult['link'])
        setattr(db_google_search_result, 'snippet', googleSearchResult['snippet'])
            
        updated_at = datetime.datetime.now()
        updated_year = str(updated_at.year)
        updated_month = str(updated_at.month)
        updated_day = str(updated_at.day)
        
        hour = updated_at.hour
        if(hour < 10):
            updated_hr = str("0"+hour)
        updated_hr = str(hour)
        minutes = updated_at.minute
        if(minutes < 10):
            updated_min = str("0"+minutes)
        updated_min = str(minutes)
        
        db_google_search_result.updated_at = updated_year+"-"+updated_month+"-"+updated_day+" "+updated_hr+":"+updated_min
        db.add(db_google_search_result)
        db.commit()
        db.refresh(db_google_search_result)
        
        return "Google Search Result Item updated successfully!"