from unittest import TestCase
from fastapi.testclient import TestClient
from src.app.main import app
from src.app.dependencies import get_repositories
from src.app.models.pickle_repository import PickleRepository
from src.core.entities.admin import Admin
from src.core.entities.buyer import Buyer
from src.core.entities.seller import Seller


class When_authenticating(TestCase):

    def setUp(self):
        self.client = TestClient(app)
        self.fake_user_repo = PickleRepository("tests/data/users.dat")

        self.fake_user_repo.clear()

        self.fake_admin = Admin(
            username="enAdministrator",
            password="abc123456",
            email_address="admin@mail.com",
            phone_number="12345678",
            first_name="Mr",
            last_name="Admin"
        )

        self.fake_buyer = Buyer(
            username="enSluttBruker",
            password="abc123456",
            email_address="buyer@mail.com",
            phone_number="12345678",
            first_name="Mr",
            last_name="Buyer"
        )

        self.fake_seller = Seller(
            username="enForhandler",
            password="abc123456",
            email_address="seller@mail.com",
            phone_number="12345678",
            company_name="Sellers Company Ltd"
        )

        self.fake_user_repo.create(self.fake_admin)
        self.fake_user_repo.create(self.fake_buyer)
        self.fake_user_repo.create(self.fake_seller)

        def fake_get_repositories():
            return {
                "users": self.fake_user_repo
            }

        app.dependency_overrides[get_repositories] = fake_get_repositories


    def tearDown(self):
        self.fake_user_repo.clear()


    def test_user_can_log_in(self):
        res = self.client.post("/api/users/login", {
            "username": self.fake_buyer.username,
            "password": self.fake_buyer.password
        })

        # Should be 200, but is 302 due to a redirect
        # Is 403 if wrong credentials are submitted
        self.assertEqual(res.status_code, 302)
        self.assertIn("user_token", res.cookies.get_dict())


    def test_user_can_log_out(self):
        res = self.client.get("/api/users/logout")

        self.assertEqual(res.status_code, 200)
        self.assertNotIn("user_token", res.cookies.get_dict())


    def test_user_can_sign_up(self):
        pass