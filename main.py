import uvicorn

import app.user.model as userModel
import app.payment.model as paymentModel
import app.googleSearchResult.model as googleSearchResult
from database import engine

userModel.Base.metadata.create_all(bind=engine)
paymentModel.Base.metadata.create_all(bind=engine)
googleSearchResult.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8081, reload=True)
