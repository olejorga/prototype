from unittest import TestCase
from src.app.models.pickle_repository import PickleRepository
from src.core.entities.entity import Entity


class Test_pickle_repository(TestCase):

    def setUp(self):
        self.repo = PickleRepository("tests/data/users.dat")
        self.repo.entities = []

        self.fake_entity = Entity()
        self.fake_entity.id = "dummy_id"
        
        self.repo.entities.append(self.fake_entity)


    def tearDown(self):
        self.repo.entities = []


    def test_can_load_entities(self):
        pass


    def test_can_save_entities(self):
        pass