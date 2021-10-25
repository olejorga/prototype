from typing import List
from ..entities.entity import Entity
from .repository import Repository


class FakeRepository(Repository):
    
    # OVERRIDE
    def create(self, entity: Entity):
        pass


    # OVERRIDE
    def read(self) -> List[Entity]:
        pass


    # OVERRIDE
    def update(self, id: str, entity: Entity):
        pass


    # OVERRIDE
    def delete(self, id: str):
        pass


    # OVERRIDE
    def find(self, id: str) -> Entity:
        pass


    # OVERRIDE
    def search(self, key: int, value: any) -> List[Entity]:
        pass