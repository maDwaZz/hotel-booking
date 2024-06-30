from typing import Type

from sqlalchemy import select

from app.database import async_session_maker, Base


class BaseDAO:
    model: Type[Base]

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()
