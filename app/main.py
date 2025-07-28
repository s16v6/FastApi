from fastapi import FastAPI, HTTPException, Query, Path
from typing import List, Optional
from app.schemas import Entity, EntityCreate, EntityUpdate
from app.models import storage

app = FastAPI(
    title="Entity API",
    description="API для управления сущностями", version="1.0.0"
    )


@app.get(
        "/entities",
        response_model=List[Entity],
        summary="Получить список сущностей"
        )
async def list_entities(
    name: Optional[str] = Query(
        None, description="Фильтр по части имени сущности"
            )
        ):
    """
    Получить список всех сущностей.
    Можно фильтровать по части имени с помощью параметра `name`..
    """
    entities = storage.list(name_filter=name)
    return entities


@app.get(
        "/entities/{entity_id}",
        response_model=Entity,
        summary="Получить одну сущность по ID"
        )
async def get_entity(
    entity_id: int = Path(..., description="ID сущности", gt=0)
        ):
    """
    Получить сущность по её уникальному идентификатору.
    """
    entity = storage.get(entity_id)
    if not entity:
        raise HTTPException(status_code=404, detail="Сущность не найдена")
    return entity


@app.post(
        "/entities",
        response_model=Entity,
        status_code=201,
        summary="Создать новую сущность"
        )
async def create_entity(entity_create: EntityCreate):
    """
    Создать новую сущность с указанными данными.
    """
    entity = storage.create(entity_create)
    return entity


@app.put(
        "/entities/{entity_id}",
        response_model=Entity,
        summary="Обновить данные сущности"
        )
async def update_entity(
    entity_id: int = Path(..., description="ID сущности для обновления", gt=0),
    entity_update: EntityUpdate = ...
):
    """
    Обновить существующую сущность.
    Можно обновить имя и/или описание.
    """
    updated_entity = storage.update(entity_id, entity_update)
    if not updated_entity:
        raise HTTPException(status_code=404, detail="Сущность не найдена")
    return updated_entity


@app.delete(
        "/entities/{entity_id}",
        status_code=204,
        summary="Удалить сущность"
        )
async def delete_entity(
    entity_id: int = Path(..., description="ID сущности для удаления", gt=0)
        ):
    """
    Удалить сущность по её ID.
    """
    deleted = storage.delete(entity_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Сущность не найдена")
    return None
