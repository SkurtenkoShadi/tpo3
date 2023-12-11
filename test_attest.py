from module import MathOperations
from module import TextOperation
import unittest

class TestMathOperations(unittest.TestCase):

    def test_square(self):
        math = MathOperations(5)
        result = math.square()
        self.assertEqual(result, 25)

    def test_cube(self):
        math = MathOperations(6)
        result = math.cube()
        self.assertEqual(result, 216)

    def test_sqrt(self):
        math = MathOperations(25)
        result = math._sqrt()
        self.assertEqual(result, 5)

    def test_sqrt_2(self):
        math = MathOperations(-5)
        result = math._sqrt()
        self.assertEqual(result, False)

class TestTextOperation(unittest.TestCase):

    def test_count_words(self):
        text = TextOperation('Hello my friend')
        result = text.count_words()
        self.assertEqual(result, 3)

    def test_symbols_count(self):
        text = TextOperation('hi, its me!')
        result = text.symbols_count()
        self.assertEqual(result, 9)

    def test_up(self):
        text = TextOperation('bye bye')
        result = text._up()
        self.assertEqual(result, 'BYE BYE')
    
if __name__ == '__main__':
    unittest.main()