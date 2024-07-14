from fastapi import APIRouter, BackgroundTasks

from app.domains.users.schemas.sign import SignUp
from app.domains.users.services.sign import SignService

router = APIRouter()

@router.post("/sign-up")
async def sign_up_(
        payload: SignUp.Request,
):
    sign_service = SignService()
    await sign_service.sign_up(payload=payload)

