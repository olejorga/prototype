from unittest import TestCase
from fastapi.testclient import TestClient
from src.app.main import app
from src.core.entities import Listing, Sale
from src.app.models.pickle_repository import PickleRepository
from src.app.dependencies import get_repositories


class When_searching(TestCase):

    @classmethod
    def setUpClass(cls):
        app = None

    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.client = TestClient(cls.app)

        cls.fake_listing_1 = Listing(
            title="Sofa", 
            price=15000, 
            description="Antikk sofa fra 1890", 
            pictures=""
        )

        cls.fake_listing_2 = Sale(
            title="Skrivemaskin", 
            price=1200, 
            description="Veldig sjelden Remington skrivemaskin i god tilstand", 
            pictures=""
        )


    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(cls):
        pass


    def tearDown(cls):
        pass


    def test_can_search_thorugh_listings(self):
        def fake_get_repositories():
            return {
                "users": PickleRepository("tests/data/listings.dat")
            }

        self.app.dependency_overrides[get_repositories] = fake_get_repositories
        pass


    def test_keyword_search(self):
        pass