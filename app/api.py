from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT

from sqlalchemy.orm import Session
import app.user.schema as userSchema
import app.payment.schema as paymentSchema
from database import get_db
from app.user.repository import UserRepo
from app.payment.repository import PaymentLogRepo
from decouple import config

from serpapi import GoogleSearch

import stripe

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

stripe.api_key = config("STRIPE_SECRET")

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
async def google_search(search_keyword: str):
    """
        Google Search with Keyword
    """
    
    search = GoogleSearch({
        "q": search_keyword,
        "location": "Austin,Texas",
        "serp_api_key": config('SerpAPI_Key_Google_Search')
    })
    
    result = search.get_dict()

    return {
        "result_search": result
    }    
    
    