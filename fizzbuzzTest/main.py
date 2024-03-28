import unittest
import task as t
class TestStartMethods(unittest.TestCase):
    '''def test_simple_condition_positive(self):
        self.assertTrue(t.simple_condition(11))
    def test_simple_condition_negative(self):
        self.assertFalse(t.simple_condition(5))
    def test_more_conditions_positive(self):
        self.assertTrue(t.more_conditions(11, 5))
    def test_more_conditions_positive_negative(self):
        self.assertTrue(t.more_conditions(5, 11))
    def test_more_conditions_negative(self):
        self.assertFalse(t.more_conditions(5, 5))
    def test_moar_conditions_positive(self):
        self.assertTrue(t.moar_conditions(110, 15))
    def test_moar_conditions_negative(self):
        self.assertFalse(t.moar_conditions(90, 15))
    def test_moar_conditions_negative1(self):
        self.assertFalse(t.moar_conditions(90, 9))
    def test_moar_conditions_negative2(self):
        self.assertFalse(t.moar_conditions(9, 9))'''
    def test_fizzbuzz_fizzbuzz(self):
        self.assertEqual(t.fizzbuzz_condition(15), "fizzbuzz")
    def test_fizzbuzz_fizz(self):
        self.assertEqual(t.fizzbuzz_condition(33), "fizz")
    def test_fizzbuzz_buzz(self):
        self.assertEqual(t.fizzbuzz_condition(35), "buzz")
    def test_fizzbuzz_none(self):
        self.assertEqual(t.fizzbuzz_condition(8), "8")
    def test_fast_sqrt_negative(self):
        with self.assertRaises(ValueError):
            t.fast_sqrt(-1)
    def test_fast_sqrt_positive(self):
        self.assertTrue(abs(t.fast_sqrt(9)- 3) < 0.05)
    


if __name__ == '__main__':
    unittest.main()