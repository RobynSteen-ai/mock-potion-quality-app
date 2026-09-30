import unittest

from app import assess_potion


class TestAssessPotionUnit(unittest.TestCase):

    def test_clear_potion_in_approved_range(self):
        result = assess_potion(6.5, "clear")

        self.assertEqual(result, "Approved")

    def test_non_text_clarity_raises_value_error(self):
        with self.assertRaises(ValueError):
            assess_potion(6.5, 123)


if __name__ == "__main__":
    unittest.main()
