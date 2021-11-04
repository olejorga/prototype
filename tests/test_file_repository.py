from unittest import TestCase
from src.core.repositories.file_repository import FileRepository
from src.core.entities.entity import Entity


class Test_file_repository(TestCase):

    def setUp(self):
        self.repo = FileRepository("")

        self.fake_entity = Entity()
        self.fake_entity.id = "dummy_id"
        
        self.repo.entities.append(self.fake_entity)


    def tearDown(self):
        self.repo.entities = []


    def test_can_create_entity(self):
        self.repo.create(self.fake_entity)
        self.assertIn(self.fake_entity, self.repo.entities)


    def test_can_read_entities(self):
        entities = self.repo.read()
        
        self.assertGreater(len(entities), 0)
        self.assertIsInstance(entities[0], Entity)


    def test_can_update_entity(self):
        new_entity = Entity()
        self.repo.update("dummy_id", new_entity)

        self.assertIs(self.repo.entities[0], new_entity)


    def test_can_delete_entity(self):
        self.repo.delete("dummy_id")
        self.assertEqual(len(self.repo.entities), 0)


    def test_can_find_entity(self):
        found_entity = self.repo.find("dummy_id")
        self.assertIs(found_entity, self.fake_entity)


    def test_can_search_entities(self):
        results = self.repo.search("id", "dummy_id")

        self.assertGreater(len(results), 0)
        self.assertIs(results[0], self.fake_entity)


    def test_can_clear_repo(self):
        self.repo.clear()
        self.assertEqual(len(self.repo.entities), 0)


    def test_can_assign_unique_id(self):
        self.repo.create(Entity())
        self.repo.create(Entity())
        
        self.assertNotEqual(self.repo.entities[1].id, self.repo.entities[2].id)