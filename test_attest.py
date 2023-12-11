from module import MathOperations
from module import TextOperation
import unittest

class TestAttest(unittest.TestCase):

    def test_first(self):
        math = MathOperations(9)
        text = TextOperation('Hello, my friend!')
        result1 = math.square()
        result2 = math.cube()
        result3 = math._sqrt()
        result4 = text.count_words()
        result5 = text.symbols_count()
        result6 = text._up()
        self.assertEqual(result1, 81)
        self.assertEqual(result2, 729)
        self.assertEqual(result3, 3.0)
        self.assertEqual(result4, 3)
        self.assertEqual(result5, 15)
        self.assertEqual(result6, "HELLO, MY FRIEND!")

    def test_second(self):
        math = MathOperations("")
        text = TextOperation('Hello friend')
        result1 = math.square()
        result2 = math.cube()
        result3 = text.count_words()
        result4 = math._sqrt()
        result5 = text.symbols_count()
        result6 = text._up()
        self.assertEqual(result1, False)
        self.assertEqual(result2, False)
        self.assertEqual(result3, 2)
        self.assertEqual(result4, False)
        self.assertEqual(result5, 11)
        self.assertEqual(result6, "HELLO FRIEND")

    def test_third(self):
        math = MathOperations(4)
        text = TextOperation("")
        result1 = math.square()
        result2 = math.cube()
        result3 = text.count_words()
        result4 = math._sqrt()
        result5 = text.symbols_count()
        result6 = text._up()
        self.assertEqual(result1, 16)
        self.assertEqual(result2, 64)
        self.assertEqual(result3, False)
        self.assertEqual(result4, 2.0)
        self.assertEqual(result5, False)
        self.assertEqual(result6, False)

    def test_fourth(self):
        math = MathOperations(-4)
        text = TextOperation("hi man")
        result1 = math.square()
        result2 = math.cube()
        result3 = text.count_words()
        result4 = math._sqrt()
        result5 = text.symbols_count()
        result6 = text._up()
        self.assertEqual(result1, 16)
        self.assertEqual(result2, -64)
        self.assertEqual(result3, 2)
        self.assertEqual(result4, False)
        self.assertEqual(result5, 5)
        self.assertEqual(result6, "HI MAN")

    if __name__ == '__main__':
        unittest.main()