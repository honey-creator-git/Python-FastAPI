from fastapi import Depends, FastAPI, HTTPException, Body, Depends

from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT

from sqlalchemy.orm import Session
import app.user.schema as schema
from database import get_db, engine
from app.user.repository import UserRepo

posts = [
    {
        "id": 1,
        "title": "Pancake",
        "content": "Lorem Ipsum ..."
    }
]

users = []

app = FastAPI()


# helpers

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


# route handlers

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your blog!"}


@app.get("/posts", tags=["posts"])
async def get_posts() -> dict:
    return { "data": posts }


@app.get("/posts/{id}", tags=["posts"])
async def get_single_post(id: int) -> dict:
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }


# @app.post("/user/signup", tags=["user"])
# async def create_user(user: UserSchema = Body(...)):
#     users.append(user)  # replace with db call, making sure to hash the password first
#     return signJWT(user.email)


# @app.post("/user/login", tags=["user"])
# async def user_login(user: UserLoginSchema = Body(...)):
#     if check_user(user):
#         return signJWT(user.email)
#     return {
#         "error": "Wrong login details!"
#     }
    
@app.post("/user/signup", tags=["User"])
async def create_user(user_request: schema.UserCreate, db: Session = Depends(get_db)):
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
async def login(user_request: schema.UserLogin, db: Session = Depends(get_db)):
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
    