import pickle
from os.path import exists
from ...core.repositories.file_repository import FileRepository
from ...core.entities.entity import Entity


class PickleRepository(FileRepository):

    def __init__(self, filepath: Entity):

        super().__init__(filepath)
    

    # OVERRIDE
    def load(self):
        if not exists(self.filepath):
            self.save()

        with open(self.filepath, "rb") as file:
            self.entities = pickle.load(file)


    # OVERRIDE
    def save(self):
        with open(self.filepath, "wb") as file:
            pickle.dump(self.entities, file)