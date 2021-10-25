from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from pysondb import db
from src.main import app
from src.models.receipt import Receipt

receipt_db = db.getDb("data/receipt.json")

client = TestClient(app)
