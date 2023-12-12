
import sys
class MathOperations:
    def __init__(self, value):
        self.value = value
    def square(self):
        if self.value == '':
            return False
        else:
            return self.value ** 2

    def cube(self):
        if self.value == '':
            return False
        else:
            return self.value ** 3
    
    def _sqrt(self):
        if self.value == '' or self.value < 0:
            return False
        else:
            return self.value ** 0.5
        
class TextOperation:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        if self.text == '':
            return False
        else:
            words = self.text.split()
            return len(words)

    def symbols_count(self):
        if self.text == '':
            return False
        else:
            symbols = self.text.replace(' ','')
            return len(symbols)
    
    def _up(self):
        if self.text == '':
            return False
        else:
            return self.text.upper()
    
    
        

if __name__ == "__main__":                 
    math = input("Введите число: ")
    text = input ("Введите текст: ")
    if math == "":
        math = MathOperations(math)
        text = TextOperation(text)
        squared_value = False
        cubed_value = False
        sqrt_value = False
    else:
        math = MathOperations(int(math))
        text = TextOperation(text)
        squared_value = math.square()
        cubed_value = math.cube()
        sqrt_value = math._sqrt()

    word_count = text.count_words()
    symbols_count = text.symbols_count()
    up = text._up() 

    print(f"Квадрат: {squared_value}")
    print(f"Куб: {cubed_value}")
    print(f"Количество слов: {word_count}")
    print(f"Корень: {sqrt_value}")
    print(f"Количество символов: {symbols_count}")
    print(f"Верхний регистр: {up}")
