from typing import Dict
from app.schemas import Entity, EntityCreate, EntityUpdate


class EntityStorage:
    def __init__(self):
        self._data: Dict[int, Entity] = {}
        self._id_counter: int = 1

    def list(self, name_filter: str = None):
        entities = list(self._data.values())
        if name_filter:
            entities = [e for e in entities if name_filter.lower() in e.name.lower()]
        return entities

    def get(self, entity_id: int) -> Entity:
        return self._data.get(entity_id)

    def create(self, entity_create: EntityCreate) -> Entity:
        entity = Entity(id=self._id_counter, **entity_create.dict())
        self._data[self._id_counter] = entity
        self._id_counter += 1
        return entity

    def update(self, entity_id: int, entity_update: EntityUpdate) -> Entity:
        entity = self._data.get(entity_id)
        if not entity:
            return None
        updated_data = entity.dict()
        update_fields = entity_update.dict(exclude_unset=True)
        updated_data.update(update_fields)
        updated_entity = Entity(**updated_data)
        self._data[entity_id] = updated_entity
        return updated_entity

    def delete(self, entity_id: int) -> bool:
        if entity_id in self._data:
            del self._data[entity_id]
            return True
        return False


storage = EntityStorage()
