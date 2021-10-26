from os import environ
from fastapi.testclient import TestClient
from ..src.app.main import app


environ["LISTINGS_REPO_PATH"] = "tests/data/listings.dat"
environ["USERS_REPO_PATH"] = "tests/data/users.dat"


client = TestClient(app)


def test_show_listings_view():
    res = client.get("/")
    assert res.status_code == 200