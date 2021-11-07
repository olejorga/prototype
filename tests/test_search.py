from unittest import TestCase
from fastapi.testclient import TestClient
from src.app.dependencies import get_repositories
from src.app.main import app
from src.app.models.pickle_repository import PickleRepository
from src.core.entities.listing import Listing


class When_searching(TestCase):

    def setUp(self):
        self.client = TestClient(app)
        self.fake_listing_repo = PickleRepository("tests/data/listings.dat")

        self.fake_listing_repo.clear()

        self.fake_listing1 = Listing(
            title="BMW",
            price=100000,
            description="A 2010 BMW",
            pictures=[""],
            user_id=""
        )

        self.fake_listing2 = Listing(
            title="VOLVO",
            price=200000,
            description="A 1984 VOLVO 240",
            pictures=[""],
            user_id=""
        )

        self.fake_listing_repo.create(self.fake_listing1)
        self.fake_listing_repo.create(self.fake_listing2)

        def fake_get_repositories():
            return {
                "listings": self.fake_listing_repo
            }

        app.dependency_overrides[get_repositories] = fake_get_repositories


    def tearDown(self):
        self.fake_listing_repo.clear()


    def test_can_search_by_title(self):
        res = self.client.get(f"/search/?input={self.fake_listing1.title}")

        self.assertEqual(res.status_code, 200)
        self.assertIn(self.fake_listing1.title, res.text)
        self.assertNotIn(self.fake_listing2.title, res.text)


    def test_can_search_by_description(self):
        res = self.client.get(f"/search/?input={self.fake_listing1.description}")

        self.assertEqual(res.status_code, 200)
        self.assertIn(self.fake_listing1.title, res.text)
        self.assertNotIn(self.fake_listing2.title, res.text)


    def test_can_search_by_keyword(self):
        res = self.client.get("/search/?input=2010")

        self.assertEqual(res.status_code, 200)
        self.assertIn(self.fake_listing1.title, res.text)
        self.assertNotIn(self.fake_listing2.title, res.text)