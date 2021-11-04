from typing import List
from ..entities.entity import Entity


class Repository:

    def create(self, entity: Entity):
        pass


    def read(self) -> List[Entity]:
        pass


    def update(self, id: str, entity: Entity):
        pass


    def delete(self, id: str):
        pass


    def find(self, id: str) -> Entity:
        pass


    def search(self, key: int, value: any) -> List[Entity]:
        pass


    def clear(self):
        pass