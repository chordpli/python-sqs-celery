import uvicorn
from fastapi import FastAPI

from app.domains.users.router.sign import router as sign_router

app = FastAPI()
app.include_router(sign_router, tags=["sign"], prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
