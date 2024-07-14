from sqlalchemy import (
    Column,
    String,
    Integer,
)

from app.edge.db.base_class import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    @staticmethod
    async def sign_up(email:str, password:str):
        return Users(
            email=email,
            password=password,
        )
