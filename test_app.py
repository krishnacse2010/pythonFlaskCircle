import os
import sys

# Add the parent directory of the current file to the path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from app import app

def test_add():
    with app.test_client() as client:
        response = client.get('/add?a=2&b=3')
        assert response.data == b'5'

def test_subtract():
    with app.test_client() as client:
        response = client.get('/subtract?a=5&b=2')
        assert response.data == b'3'
