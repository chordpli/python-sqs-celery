from app.domains.users.models.users import Users
from app.domains.users.schemas.sign import SignUp
from app.domains.email.worker.email import send_welcome_email


class SignService:

    async def sign_up(self, payload: SignUp.Request):
        print("SIGN UP")
        user = await Users.sign_up(email=payload.email, password=payload.password)
        result = send_welcome_email.apply_async(args=[payload.email])
        print("task: ", result)

        return SignUp.Response.from_orm(user=user)

