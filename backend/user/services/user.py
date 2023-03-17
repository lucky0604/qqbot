from typing import Optional, List
from sqlalchemy import or_, select, and_

from backend.user.models import User
from core.db import Transactional, session
from core.exceptions import (
    DuplicateValueException, )


class UserService:

    def __init__(self):
        ...

    async def get_user_list(
        self,
        limit: int = 10,
        prev: Optional[int] = None,
    ) -> List[User]:
        query = select(User)
        if prev:
            query = query.where(User.id < prev)

        if limit > 10:
            limit = 10
        query = query.limit(limit)
        result = await session.execute(query)
        return result.scalars().all()

    @Transactional()
    async def create_user(self, nickname: str) -> None:
        ...
