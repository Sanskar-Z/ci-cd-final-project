import unittest
from service.app import app, counters


class CounterServiceTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        counters.clear()

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "healthy")

    def test_create_and_increment_counter(self):
        response = self.client.post("/counters/demo")
        self.assertEqual(response.status_code, 201)
        response = self.client.put("/counters/demo")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["value"], 1)

    def test_missing_counter_returns_404(self):
        response = self.client.get("/counters/missing")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
