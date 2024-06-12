from fastapi import FastAPI
import uvicorn
from api import user, admin, authentication

app = FastAPI(title="MY JOBS")

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(admin.router)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
