from unittest import TestCase
from fastapi.testclient import TestClient
from src.app.main import app


class WhenSomething(TestCase):

    def setUp(self):
        self.client = TestClient(app)


    def test_something(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)


    def tearDown(self):
        pass