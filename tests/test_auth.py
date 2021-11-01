from unittest import TestCase
from fastapi import Request
from fastapi.testclient import TestClient
from src.app.main import app
from src.app.dependencies import get_current_user, get_repositories
from src.app.models.pickle_repository import PickleRepository
from src.core.entities.admin import Admin
from src.core.entities.buyer import Buyer
from src.core.entities.seller import Seller


class When_authenticating(TestCase):
    app = None

    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.client = TestClient(cls.app)

        cls.fake_admin = Admin(
            username="enAdministrator",
            password="abc123456",
            email_address="admin@mail.com",
            phone_number="12345678",
            first_name="Mr",
            last_name="Admin"
        )

        cls.fake_buyer = Buyer(
            username="enSluttBruker",
            password="abc123456",
            email_address="buyer@mail.com",
            phone_number="12345678",
            first_name="Mr",
            last_name="Buyer"
        )

        cls.fake_seller = Seller(
            username="enForhandler",
            password="abc123456",
            email_address="seller@mail.com",
            phone_number="12345678",
            company_name="Sellers Company Ltd"
        )

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(cls):
        pass

    def tearDown(cls):
        pass

    def test_any_legitimate_user_can_log_in(self):
        def fake_get_repositories():
            return {
                "users": PickleRepository("tests/data/users.dat")
            }

        self.app.dependency_overrides[get_repositories] = fake_get_repositories

        res = self.client.post("/api/users/login", {"username": self.fake_buyer.username,
                                                    "password": self.fake_buyer.password})

        self.assertEqual(res.status_code, 200)

    def test_any_legitimate_user_can_log_out(self):
        pass

    def test_buyer_can_sign_up(self):
        pass

    def test_seller_can_apply(self):
        pass
