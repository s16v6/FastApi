from pydantic import BaseModel, Field
from typing import Optional


class EntityBase(BaseModel):
    name: str = Field(..., example="Sample Entity")
    description: Optional[str] = Field(None, example="Описание сущности")


class EntityCreate(EntityBase):
    pass


class EntityUpdate(BaseModel):
    name: Optional[str] = Field(None, example="Updated Name")
    description: Optional[str] = Field(None, example="Обновленное описание")


class Entity(EntityBase):
    id: int = Field(..., example=1)

    class Config:
        orm_mode = True
