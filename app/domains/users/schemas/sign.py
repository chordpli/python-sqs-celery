from pydantic import BaseModel

from app.domains.users.models.users import Users


class SignUp():
    class Request(BaseModel):
        email: str
        password: str

    class Response(BaseModel):
        email: str

        @classmethod
        def from_orm(cls, user: Users):
            return cls(
                email=user.email
            )
