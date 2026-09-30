import unittest

from app import app


class TestPotionAppIntegration(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_valid_assessment_returns_approved(self):
        response = self.client.post(
            "/assess",
            json={"ph": 6.5, "clarity": "clear"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"], "Approved")

    def test_non_text_clarity_returns_400(self):
        response = self.client.post(
            "/assess",
            json={"ph": 6.5, "clarity": 123},
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())


if __name__ == "__main__":
    unittest.main()
