"""
Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты:

- value - текущее значение счетчика

Определить методы:

- инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
- increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
- decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
- метод __iter__
- метод __next__
"""


class Counter:
    value: int

    def __init__(self, value: int = 0):
        self.value = value

    @classmethod
    def increase(cls):
        cls.value += 1
        return cls.value

    @classmethod
    def decrease(cls):
        cls.value -= 1
        return cls.value

    def __iter__(self):
        return iter(self.value)

    def __next__(self):
        return next(self.value)

Counter.value = 0
print(Counter.value)

print(Counter.increase())

for value in Counter.value:
    print(value)



