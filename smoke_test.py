import unittest

from app import app


class TestPotionAppSmoke(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_health_endpoint_is_available(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "healthy"})

    def test_home_endpoint_is_available(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["application"],
            "Potion Quality App",
        )


if __name__ == "__main__":
    unittest.main()
