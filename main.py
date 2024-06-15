from fastapi import FastAPI
import uvicorn
from api import user, recruiter, authentication

app = FastAPI(title="MY JOBS")

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(recruiter.router)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
