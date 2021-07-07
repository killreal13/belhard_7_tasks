"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n
- метод generate, который принимает длину последовательности n
- метод print_seq, который выводит последовательность на экран
"""


class RandSequence:
    sequence = []

    def __init__(self, n):
        self.n = n

    def generate(self):
        for i in range(self.n):
            self.sequence.append(i)
        return self.sequence

    def print_seq(self):
        print(self.sequence)