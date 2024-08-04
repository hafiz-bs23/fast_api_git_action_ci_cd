from fastapi.testclient import TestClient

from .app import app 

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    
def test_app_sayOMG():
    response = client.get("/omg")
    assert response.status_code == 200
    assert response.json() == {"data": "Oh my F***ing god it is working"}
    
def test_app_sayOMG_Not_Found():
    response = client.get("/omg")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}