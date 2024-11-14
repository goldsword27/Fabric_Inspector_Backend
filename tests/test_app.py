import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestApp(unittest.TestCase):
    def test_root(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Kumaş delik tespit API'sine hoş geldiniz."})

    def test_detect_endpoint(self):
        # Bu testte modelin gerçekte mevcut olmaması nedeniyle gerçek bir test yapamıyoruz
        # Ancak endpoint'in varlığını test edebiliriz
        response = client.post("/detect")
        self.assertIn(response.status_code, [200, 400])

if __name__ == '__main__':
    unittest.main()
