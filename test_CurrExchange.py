import unittest
from CurrExchange import convert, get_rate


class TestCurrExchange(unittest.TestCase):

    def test_convert_normal(self):
        self.assertEqual(convert(100, 13.4), 1340.0)

    def test_convert_zero(self):
        self.assertEqual(convert(0, 13.4), 0.0)

    def test_convert_float(self):
        self.assertAlmostEqual(convert(2.5, 1.2), 3.0)

    def test_get_rate_found(self):
        fake_data = {'quotes': {'USDGHS': 13.4}}
        self.assertEqual(get_rate(fake_data, 'GHS'), 13.4)

    def test_get_rate_missing(self):
        fake_data = {'quotes': {'USDGHS': 13.4}}
        self.assertIsNone(get_rate(fake_data, 'XYZ'))


if __name__ == '__main__':
    unittest.main()
