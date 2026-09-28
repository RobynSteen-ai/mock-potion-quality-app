import unittest

from app import assess_potion


class TestAssessPotion(unittest.TestCase):

    def test_approved_potion(self):
        self.assertEqual(assess_potion(6.5, "clear"), "Approved")

    def test_lower_approved_boundary(self):
        self.assertEqual(assess_potion(5.5, "clear"), "Approved")

    def test_review_required_for_cloudy_potion(self):
        self.assertEqual(
            assess_potion(6.5, "cloudy"),
            "Review Required",
        )

    def test_review_required_for_high_ph(self):
        self.assertEqual(
            assess_potion(8.0, "clear"),
            "Review Required",
        )

    def test_rejected_potion(self):
        self.assertEqual(assess_potion(2.0, "cloudy"), "Rejected")

    def test_invalid_ph_raises_error(self):
        with self.assertRaisesRegex(
            ValueError,
            "pH must be between 0 and 14",
        ):
            assess_potion(15, "clear")

    def test_invalid_clarity_raises_error(self):
        with self.assertRaisesRegex(
            ValueError,
            "Clarity must be clear or cloudy",
        ):
            assess_potion(7.0, "sparkly")


if __name__ == "__main__":
    unittest.main()
