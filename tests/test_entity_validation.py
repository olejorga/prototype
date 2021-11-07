from unittest import TestCase
from src.core.entities.listing import Listing
from src.core.entities.user import User


class Test_entity_validation(TestCase):

    def setUp(self):
        self.fake_listing = Listing(
            title="Some title",
            price=100,
            description="",
            pictures=[""],
            user_id=""
        )

        self.fake_user = User(
            username="Redoc",
            password="abc123456",
            email_address="redoc@mail.org",
            phone_number="99001122"
        )


    def tearDown(self):
        pass


    def test_listing_title_is_valid(self):
        try:
            self.fake_listing.set_title("An awesome title")
            self.fake_listing.set_title("50 An awesome title")
        except:
            self.fail("Invalid title")
        finally:
            self.assertRaises(ValueError, self.fake_listing.set_title, "")
            self.assertRaises(ValueError, self.fake_listing.set_title, "Some_title")
            self.assertRaises(ValueError, self.fake_listing.set_title, "@Some title")


    def test_listing_price_is_valid(self):
        try:
            self.fake_listing.set_price(1)
            self.fake_listing.set_price(0)
        except:
            self.fail("Invalid price")
        finally:
            self.assertRaises(ValueError, self.fake_listing.set_price, -1)


    def test_user_username_is_valid(self):
        try:
            self.fake_user.set_username("Beast")
            self.fake_user.set_username("Beast123")
            self.fake_user.set_username("123")
            self.fake_user.set_username("123-beast_zzz")
        except:
            self.fail("Invalid username")
        finally:
            self.assertRaises(ValueError, self.fake_user.set_username, "")
            self.assertRaises(ValueError, self.fake_user.set_username, "beast 123")
            self.assertRaises(ValueError, self.fake_user.set_username, "@beast")


    def test_user_password_is_valid(self):
        try:
            self.fake_user.set_password("12345cde")
            self.fake_user.set_password("a_some_1")
        except:
            self.fail("Invalid password")
        finally:
            self.assertRaises(ValueError, self.fake_user.set_password, "")
            self.assertRaises(ValueError, self.fake_user.set_password, "abc123")
            self.assertRaises(ValueError, self.fake_user.set_password, "\{abc123456\}")
            self.assertRaises(ValueError, self.fake_user.set_password, "abc123æøå")


    def test_user_email_address_is_valid(self):
        try:
            self.fake_user.set_email_address("mail@mail.com")
        except:
            self.fail("Invalid email address")
        finally:
            self.assertRaises(ValueError, self.fake_user.set_email_address, "")
            self.assertRaises(ValueError, self.fake_user.set_email_address, "mail@")
            self.assertRaises(ValueError, self.fake_user.set_email_address, "exp@mail")
            self.assertRaises(ValueError, self.fake_user.set_email_address, "@mail.com")


    def test_phone_number_is_valid(self):
        try:
            self.fake_user.set_phone_number("44556677")
        except:
            self.fail("Invalid phone number")
        finally:
            self.assertRaises(ValueError, self.fake_user.set_phone_number, "")
            self.assertRaises(ValueError, self.fake_user.set_phone_number, "aabbccdd")
            self.assertRaises(ValueError, self.fake_user.set_phone_number, "++__--@@")
            self.assertRaises(ValueError, self.fake_user.set_phone_number, "aabb9922")