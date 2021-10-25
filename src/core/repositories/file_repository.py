import uuid
from typing import List
from .repository import Repository
from ..entities.entity import Entity


class FileRepository(Repository):

    def __init__(self, filepath: str):

        self.filepath = filepath
        self.entities = []

        self.load()


    # OVERRIDE
    def create(self, entity: Entity):
        entity.id = self.assign_id()
        self.entities.append(entity)

        self.save()


    # OVERRIDE
    def read(self) -> List[Entity]:
        return self.entities


    # OVERRIDE
    def update(self, id: str, entity: Entity):
        self.delete(id)

        entity.id = id
        self.create(entity)


    # OVERRIDE
    def delete(self, id: str):
        entity = self.find(id)

        if entity is not None:
            self.entities.remove(entity)
            self.save()


    # OVERRIDE
    def find(self, id: str) -> Entity:
        self.load()

        for entity in self.entities:
            if entity.id == id:
                return entity

        return None


    # OVERRIDE
    def search(self, key: int, value: any) -> List[Entity]:
        results = []

        self.load()

        for entity in self.entities:
            if entity.__dict__[key] == value:
                results.append(entity)

        return results


    def assign_id(self) -> str:
        id = uuid.uuid1()
        
        if self.find(id) is not None :
            return self.assign_id()

        return str(id)


    def load(self):
        pass


    def save(self):
        pass