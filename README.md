![Build Status](https://github.com/SkurtenkoShadi/tpo3/actions/workflows/tester.yml/badge.svg?branch=master)
![CI/CD GitHub Actions](https://github.com/SkurtenkoShadi/tpo3/actions/workflows/tester.yml/badge.svg)
# План тестирования:

# Аттестационное тестирование
- Тест А1 (положительный)
- Начальное состояние: Открытый терминал
- Действие: Пользователь запускает программу и вводит: 9 и Hello, my friend!
- Ожидаемый результат:
```
Введите число: 9
Введите текст: Hello, my friend!
Квадрат: 81       
Куб: 729
Количество слов: 3
Корень: 3.0       
Количество символов: 15
Верхний регистр: HELLO, MY FRIEND!
```
- Тест А2 (негативный)
- Начальное состояние: Открытый терминал
- Действие: Пользователь запускает программу и вводит: Hello friend
- Ожидаемый результат:
```
Квадрат: False
Куб: False
Количество слов: 2
Корень: False
Количество символов: 11
Верхний регистр: HELLO FRIEND
```
- Тест А3 (негативный)
- Начальное состояние: Открытый терминал
- Действие: Пользователь запускает программу и вводит: 4
- Ожидаемый результат:
```
Квадрат: 16
Куб: 64
Количество слов: False
Корень: 2.0
Количество символов: False
Верхний регистр: False
```
- Тест А4 (негативный)
- Начальное состояние: Открытый терминал
- Действие: Пользователь запускает программу и вводит: -4 и hi man
- Ожидаемый результат:
```
Квадрат: 16
Куб: -64
Количество слов: 2
Корень: False
Количество символов: 5
Верхний регистр: HI MAN
```

# Блочное тестирование
<ol>
<li>
<h3>Класс TestMathOperations</h3>
<ol>
<li>
<h4>Метод square(self), тест test_square(self) (положительный)</h4>
<ul>
<li>Входные данные: 5</li>
<li>Ожидаемый результат: 25</li>
</ul>
</li>
<li>
<h4>Метод cube(self), тест test_cube(self) (положительный)</h4>
<ul>
<li>Входные данные: 6</li>
<li>Ожидаемый результат: 216</li>
</ul>
</li>
<li>
<h4>Метод _sqrt(self), тест test_sqrt(self) (положительный)</h4>
<ul>
<li>Входные данные: 25</li>
<li>Ожидаемый результат: 5</li>
</ul>
</li>
<li>
<h4>Метод _sqrt(self), тест test_sqrt(self) (негативный)</h4>
<ul>
<li>Входные данные: -5</li>
<li>Ожидаемый результат: False</li>
</ul>
</li>
</ol>
</li>
<li>
<h2>Класс TestTextOperation</h2>
<ol>
<li>
<h4>Модуль count_words, тест test_count_words (положительный)</h4>
<ul>
<li>Входные данные: Hello my friend</li>
<li>Ожидаемый результат: 3</li>
</ul>
</li>
<li>
<h4>Модуль symbols_count, тест test_symbols_count (положительный)</h4>
<ul>
<li>Входные данные: hi, its me!</li>
<li>Ожидаемый результат: 9</li>
</ul>
</li>
<li>
<h4>Модуль _up, тест test_up (положительный)</h4>
<ul>
<li>Входные данные: bye bye</li>
<li>
Ожидаемый результат: BYE BYE
</li>
</ul>
</li>
<li>
<h4>Модуль count_words_2, тест test_count_words_2 (отрицательный)</h4>
<ul>
<li>Входные данные: пустая строка</li>
<li>Ожидаемый результат: False</li>
</ul>
</li>
</ol>
</li>
</ol>

# Интеграционное тестирование
<ol>
<li>
<h3>Тест test_int_first</h3>
<ul>
<li>Классы: TextOperation, MathOperations.  Методы: count_words(), symbols_count(), _up(), square(), cube(), _sqrt()</li>
<li>Описание: Проверяем, можно ли использовать результат работы метода count words в методах square(), cube(), _sqrt()</li>
<li>Входные данные: Hello, my dear friend!</li>
<li>Ожидаемый результат: 
Квадрат: 16
Куб: 64
Количество слов: 4
Корень: 2.0
Количество символов: 19
Верхний регистр: HELLO, MY DEAR FRIEND!</li>
</ul>
</li>

</ol>
