from pydantic import BaseModel, Field


class CreateUserRequestSchema(BaseModel):
    nickname: str = Field(..., description="Nickname")