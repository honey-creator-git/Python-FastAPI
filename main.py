import uvicorn

import app.user.model as model
from database import engine

model.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8081, reload=True)
