from module import MathOperations
from module import TextOperation
import unittest

class TestIntegt(unittest.TestCase):
    def test_int_first(self):
        text = TextOperation('Hello, my dear friend!')
        result1 = text.count_words()
        result2 = text.symbols_count()
        result3 = text._up()
        math = MathOperations(result1)
        result4 = math.square()
        result5 = math.cube()
        result6 = math._sqrt()
        self.assertEqual(result4, 16)
        self.assertEqual(result5, 64)
        self.assertEqual(result6, 2)
        self.assertEqual(result1, 4)
        self.assertEqual(result2, 19)
        self.assertEqual(result3, "HELLO, MY DEAR FRIEND!")