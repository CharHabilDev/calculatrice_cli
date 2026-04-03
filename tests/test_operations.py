import unittest


from src.operations import (
    addition,
    soustraction,
    multiplication,
    division,
    puissance,
    racine_carree
)


class TestOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(7, 2), 9)

    def test_addition_negative(self):
        self.assertEqual(addition(-8, 2), -6)

    def test_soustraction(self):
        self.assertEqual(soustraction(8, 3), 5)

    def test_multiplication(self):
        self.assertEqual(multiplication(5, 4), 20)

    def test_multiplication_par_zero(self):
        self.assertEqual(multiplication(8, 0), 0)

    def test_division(self):
        self.assertAlmostEqual(division(100, 10), 10)

    def test_division_par_zero(self):
        with self.assertRaises(ValueError):
            division(8, 0)

    def test_puissance(self):
        self.assertEqual(puissance(6, 2), 36)

    def test_racine_carree(self):
        self.assertAlmostEqual(racine_carree(4), 2)

    def test_racine_carre_negative(self):
        with self.assertRaises(ValueError):
            racine_carree(-9)