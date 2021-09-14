import unittest
from strblackout import blackout


class TestBlackout(unittest.TestCase):
    def test_blackout_default(self):
        self.assertEqual(blackout("123456789"), "123456789")

    def test_blackout_left(self):
        self.assertEqual(blackout("123456789", left=5), "*****6789")

    def test_blackout_right(self):
        self.assertEqual(blackout("123456789", right=3), "123456***")

    def test_blackout_replacement(self):
        self.assertEqual(blackout("123456789", left=3, replacement="x"), "xxx456789")

    def test_blackout_short_text(self):
        self.assertEqual(blackout("123", left=10, right=20), "***")


if __name__ == "__main__":
    unittest.main()
