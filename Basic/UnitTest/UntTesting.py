import unittest
import MyClass

class ErrorsTests(unittest.TestCase):

    def test_calc_square(self):
        result = MyClass.calc_square(10, 10, 10)
        self.assertTrue(result > 40, 'Error result')

if __name__ == '__main__':
    unittest.main()