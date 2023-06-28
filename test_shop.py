import unittest
from shop import purchase, retry_purchase, ThreeFailedAttempts

class TestingPurchase(unittest.TestCase):

    def test_purchase_with_enough_money(self):
        self.assertEqual(True, purchase(item="top", balance=100))

    def test_purchase_with_not_enough_money(self):
        self.assertFalse(purchase(item="dress", balance=100))

    def test_purchase_with_negative_money(self):
        self.assertEqual(False, purchase(item="top", balance=-100))

    def test_purchase_with_just_enough_money(self):
        self.assertTrue(purchase(item="dress", balance=150))

class TestingRetryPurchase(unittest.TestCase):

    def test_retrypurchase_too_many_attempts(self):
        with self.assertRaises(ThreeFailedAttempts):
            retry_purchase(item="dress", balance=100, attempts=3),

if __name__ == '__main__':
    unittest.main()