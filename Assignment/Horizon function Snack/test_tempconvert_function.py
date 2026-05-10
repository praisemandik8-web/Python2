import unittest
from unittest import TestCase
from tempconvert_function import farenheit_celsius, celsius_farenheit


class TestTemperatureConversion(unittest.TestCase):

    
    def test_f_to_c_freezing(self):
        result, message = farenheit_celsius(32)

        self.assertAlmostEqual(result, 0)
        self.assertEqual(message, "Cold advisory")

    def test_f_to_c_boiling(self):
        result, message = farenheit_celsius(212)
        self.assertAlmostEqual(result, 100)
        self.assertEqual(message, "Heat alert!")

    def test_f_to_c_normal(self):
        result, message = farenheit_celsius(68)
        self.assertAlmostEqual(result, 20.0)
        self.assertEqual(message, "Temperature is not above or below threshold")

    
    def test_c_to_f_freezing(self):
        result, message = celsius_farenheit(0)
        self.assertAlmostEqual(result, 32)
        self.assertEqual(message, "Cold advisory")

    def test_c_to_f_boiling(self):
        result, message = celsius_farenheit(100)
        self.assertAlmostEqual(result, 212)
        self.assertEqual(message, "Heat alert!")

    def test_c_to_f_normal(self):
        result, message = celsius_farenheit(25)
        self.assertAlmostEqual(result, 77)
        self.assertEqual(message, "Temperature is not above or below threshold")



