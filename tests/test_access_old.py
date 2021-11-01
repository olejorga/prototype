from unittest import TestCase
from fastapi import Request
from fastapi.testclient import TestClient
from src.app.main import app
from src.app.dependencies import get_current_user
from src.core.entities.admin import Admin
from src.core.entities.buyer import Buyer
from src.core.entities.seller import Seller


class When_opening_create_listing_page(TestCase):

    def setUp(self):
        self.app = app
        self.client = TestClient(self.app)

        self.fake_admin = Admin(
            username="Admin",
            password="abcdefgh",
            email_address="admin@mail.com",
            phone_number="12345678",
            first_name="Mr",
            last_name="Admin"
        )

        self.fake_buyer = Buyer(
            username="Buyer",
            password="abcdefgh",
            email_address="buyer@mail.com",
            phone_number="12345678",
            first_name="Mr",
            last_name="Buyer"
        )

        self.fake_seller = Seller(
            username="Seller",
            password="abcdefgh",
            email_address="seller@mail.com",
            phone_number="12345678",
            company_name="Sellers Company Ltd"
        )


    def test_that_seller_have_access(self):
        async def fake_get_current_user(request: Request):
            request.state.current_user = self.fake_seller

        self.app.dependency_overrides[get_current_user] = fake_get_current_user
    
        res = self.client.get("/listings/new")

        self.assertEqual(res.status_code, 200)


    def test_that_buyer_have_no_access(self):
        async def fake_get_current_user(request: Request):
            request.state.current_user = self.fake_buyer

        self.app.dependency_overrides[get_current_user] = fake_get_current_user
    
        res = self.client.get("/listings/new")

        self.assertEqual(res.status_code, 403)


    def tearDown(self):
        pass
