from unittest import TestCase
from fastapi import Request
from fastapi.testclient import TestClient
from src.app.main import app
from src.app.dependencies import get_repositories, get_current_user
from src.app.models.pickle_repository import PickleRepository
from src.core.entities.sale import Sale
from src.core.entities.buyer import Buyer
from src.core.entities.seller import Seller


class When_buying_a_listing(TestCase):

    def setUp(self):
        self.client = TestClient(app)
        self.fake_listing_repo = PickleRepository("tests/data/listings.dat")
        self.fake_receipts_repo = PickleRepository("tests/data/receipts.dat")

        self.fake_listing_repo.clear()
        self.fake_receipts_repo.clear()

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

        self.fake_sale = Sale(
            title="Bugatti 1931",
            price=6200000,
            description="1931 Bugatti type 41",
            pictures=["https://picture.jpg"],
            user_id=""
        )

        self.fake_listing_repo.create(self.fake_sale)

        def fake_get_repositories():
            return {
                "listings": self.fake_listing_repo,
                "receipts": self.fake_receipts_repo
            }

        app.dependency_overrides[get_repositories] = fake_get_repositories


    def tearDown(self):
        self.fake_listing_repo.clear()
        self.fake_receipts_repo.clear()


    def test_buyer_can_access_checkout(self):
        async def fake_get_current_user(request: Request):
            request.state.current_user = self.fake_buyer
        
        app.dependency_overrides[get_current_user] = fake_get_current_user

        listing_id = self.fake_listing_repo.entities[0].id

        res = self.client.post("/api/checkout/" + listing_id)

        self.assertEqual(res.status_code, 302)


    def test_seller_can_not_access_checkout(self):
        async def fake_get_current_user(request: Request):
            request.state.current_user = self.fake_seller
        
        app.dependency_overrides[get_current_user] = fake_get_current_user

        listing_id = self.fake_listing_repo.entities[0].id

        res = self.client.post("/api/checkout/" + listing_id)

        self.assertEqual(res.status_code, 403)


    def test_buyer_can_place_order(self):
        self.fake_buyer.id = "dummy_id"

        async def fake_get_current_user(request: Request):
            request.state.current_user = self.fake_buyer
        
        app.dependency_overrides[get_current_user] = fake_get_current_user

        listing_id = self.fake_listing_repo.entities[0].id

        res = self.client.get("/api/receipts/" + listing_id)

        receipts = self.fake_receipts_repo.search("user_id", "dummy_id")

        self.assertEqual(res.status_code, 200)
        self.assertGreater(len(receipts), 0)


    def test_seller_can_not_place_order(self):
        self.fake_seller.id = "dummy_id"

        async def fake_get_current_user(request: Request):
            request.state.current_user = self.fake_seller
        
        app.dependency_overrides[get_current_user] = fake_get_current_user

        listing_id = self.fake_listing_repo.entities[0].id

        res = self.client.get("/api/receipts/" + listing_id)

        receipts = self.fake_receipts_repo.search("user_id", "dummy_id")

        self.assertEqual(res.status_code, 403)
        self.assertEqual(len(receipts), 0)


    def test_payment_process(self):
        #TODO: Waiting for a payment handler ;)
        pass