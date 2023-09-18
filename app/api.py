from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT
from sqlalchemy.orm import Session
from database import get_db
from app.user.repository import UserRepo
from app.payment.repository import PaymentLogRepo
from app.googleSearchResult.repository import GoogleSearchResult
from app.sentimentResult.repository import SentimentResult
from decouple import config
from serpapi import GoogleSearch
from transformers import pipeline

import app.user.schema as userSchema
import app.payment.schema as paymentSchema
import app.intervention.schema as interventionSchema
import app.messaging.schema as messagingSchema
import stripe

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sentiment_pipeline = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

stripe.api_key = config("STRIPE_SECRET")

def analysis_sentiment(text):
    data = [text]
    analysis = sentiment_pipeline(data)[0]
    response = { "text": text, "label": analysis['label'], "score": analysis['score'] }
    
    return response

# route handlers
    
@app.post("/user/signup", tags=["User"])
async def create_user(user_request: userSchema.UserCreate, db: Session = Depends(get_db)):
    """
        Create a User and store it in the database
    """
    
    db_user = await UserRepo.fetch_by_email(db, email=user_request.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists!")
    
    created_user = await UserRepo.create(db=db, user=user_request)
    jwt = signJWT(user_request.email)
    return {
        "user": created_user,
        "jwt": jwt
    }
    
@app.post("/user/login", tags=["User"])
async def login(user_request: userSchema.UserLogin, db: Session = Depends(get_db)):
    """
        Login User with Email and Password
    """
    
    db_user = await UserRepo.fetch_by_email_password(db, email=user_request.email, password=user_request.password)
    if db_user != "User not exist" and db_user != "Password is not correct":
        jwt = signJWT(user_request.email)
        return {
            "user": db_user,
            "jwt": jwt
        }
    
    return {
        "status": db_user
    }
    
@app.put("/user/update/{user_id}", dependencies=[Depends(JWTBearer())], tags=["User"])
async def update_user(user_id: int, user_request: userSchema.UserUpdate, db: Session = Depends(get_db)):
    """
        Update User with id
    """
    
    db_user = await UserRepo.update_user_by_id(db, user=user_request, id=user_id)
    if db_user != "User not exist to update":
        return {
            "updated_user": db_user
        }
    return {
        "status": db_user
    }

    
@app.post("/checkout", dependencies=[Depends(JWTBearer())], tags=["Payment"])
async def create_payment(checkout_request: paymentSchema.CheckOut):
    """
        Get Stripe Client Secret
    """
    try:
        intent = stripe.PaymentIntent.create(
            amount = checkout_request.amount * 100,
            currency = "JPY",
        )
        
        client_secret = intent['client_secret']
        return {
            "client_secret": client_secret
        }
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/paymentLog", dependencies=[Depends(JWTBearer())], tags=["Payment"])
async def payment_log(paymentLog_request: paymentSchema.PaymentLog, db: Session=Depends(get_db)):
    """
        Keep Payment Log for Users
    """
    
    payment_log = await PaymentLogRepo.create(db=db, paymentLog=paymentLog_request)
    return {
        "payment_log": payment_log
    }

@app.get("/googleSearch/{search_keyword}", dependencies=[Depends(JWTBearer())], tags=["GoogleSearch"])
async def google_search(search_keyword: str, start:int, num: int, db: Session=Depends(get_db)):
    """
        Google Search with Keyword
    """
    if num:
        search = GoogleSearch({
            "q": search_keyword,
            "location": "Austin,Texas",
            "serp_api_key": config('SerpAPI_Key_Google_Search'),
            "start": start,
            "num": num
        })
        
        search_result = search.get_dictionary()
        
        search_id = search_result.get("search_metadata").get("id")
        
        organic_results = search_result.get('organic_results')
        
        count = 0
        
        while(count < len(organic_results)):
            organic_result = organic_results[count]
            googleSearchResult = {
                "search_id": search_id,
                "title": organic_result["title"],
                "link": organic_result["link"],
                "snippet": organic_result["snippet"]
            }
            sentiment_result = analysis_sentiment(googleSearchResult["snippet"])
            sentimentResult = {
                "keyword": googleSearchResult["snippet"],
                "label": sentiment_result["label"],
                "score": str(sentiment_result["score"])
            }
            createdSentimentResult = await SentimentResult.create(db=db, sentimentResult=sentimentResult)
            createdGoogleSearchResult = await GoogleSearchResult.create(db=db, googleSearchResult=googleSearchResult)
            print("Created_Google_Search_Result => ", createdGoogleSearchResult)
            print("Created Sentiment Result => ", createdSentimentResult)
            
            count = count + 1

        return {
            "search_id": search_id,
            "status": "Search successfully!!!"
        }
        
@app.get("/sentiment_analysis", dependencies=[Depends(JWTBearer())], tags=["SentimentAnalysis"])
async def get_sentiment_result(page: int, limit: int, db: Session=Depends(get_db)):
    """
        Get the Sentiment Analysis Results
    """
    
    db_sentiment_analysis_result = await SentimentResult.get(db=db, page=page, limit=limit)
    
    return db_sentiment_analysis_result

@app.post("/handle_intervention", dependencies=[Depends(JWTBearer())], tags=["Intervention"])
async def handle_intervention(handleInterventionRequest:interventionSchema.HandleIntervention, db: Session = Depends(get_db)):
    """
        Handle Intervention
    """
    
    return True

@app.post("/handle_message", dependencies=[Depends(JWTBearer())], tags=["Messaging"])
async def handle_message(handleMessageRequest: messagingSchema.Messaging, db: Session = Depends(get_db)):
    """
        Handle Messaging
    """
    
    return True

@app.get("/get_paymentLog", dependencies=[Depends(JWTBearer())], tags=["Payment"])
async def get_payment_log(start: int, limit: int, db: Session = Depends(get_db)):
    """
        Get Payment Logs with start and limit
    """
    
    paymentLogs = await PaymentLogRepo.get(db=db, start=start, limit=limit)
    return paymentLogs
    