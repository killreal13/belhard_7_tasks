"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""


class Phone:
    brand: str
    model: str
    issue_year: int

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    @staticmethod
    def receive_call(name: str):
        print(f'Звонит {name}')

    def get_info(self):
        new_tuple = (self.brand, self.model, self.issue_year)
        return new_tuple

    def __str__(self):
        print(f'Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}')










