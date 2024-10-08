from types import NoneType


class Vehicle:
    """Базовый класс Транспорт"""
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']   # список допустимых цветов транспорта
    owner = None
    __model = None
    __color = None
    __engine_power = None


    def __init__(self, owner, model, color, engine):
        self.owner = owner              # владелец транспорта
        self.__model = model            # модель (марка) транспорта
        self.__engine_power = engine    # мощность двигателя
        self.__color = color            # цвет транспорта
        self.convert_color()            # приведем допустимые цвета к нижнему регистру

    def convert_color(self):
        """Метод приводит названия допустимых цветов к нижнему регистру"""
        i = 0
        while i < len(self.__COLOR_VARIANTS):
            self.__COLOR_VARIANTS[i] = self.__COLOR_VARIANTS[i].upper()
            i += 1

    def get_model(self):
        """Метод возвращает модель транспорта"""
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        """Метод возвращает мощность двигателя транспорта"""
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):        # возвращает строку: "Цвет: <цвет транспорта>"
        """Метод возвращает цвет транспорта"""
        return f'Цвет: {self.__color}'

    def print_info(self):       #  распечатывает результаты методов (в том же порядке):
        """Метод выводит в консоль информацию о транспорте"""
        print(self.get_model())         # Модель транспортного средства
        print(self.get_horsepower())    # Мощность двигателя
        print(self.get_color())         # Цвет транспортного средства
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        """Метод устанавливает новый цвет транспорта при условии,
        что новый свет содержится в списке допустимых цветов"""
        if new_color.upper() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    """Дочерний класс транспорта с типом кузова Sedan"""
    __PASSENGERS_LIMIT = 5      # Свойство содержит максимальное количество пассажиров для данного класса

if __name__ == '__main__':
    # Исходный код:
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)  # создаем экземпляр класса Sedan

    vehicle1.print_info()  # Выводим в консоль изначальные свойства объекта

    vehicle1.set_color('Pink')  # попытка изменить цвет на недопустимый
    vehicle1.set_color('BLACK')  # попытка изменить цвет на допустимый
    vehicle1.owner = 'Vasyok'  # смена владельца транспортного средства

    vehicle1.print_info()  # Выводим в консоль, что поменялось


# Здравствуйте, Юрий!
# Хорошее решение, однако есть несколько недочетов, которые следует исправить:
# 1. В методе `set_color` нужно проверять значение в списке __COLOR_VARIANTS без учета регистра.
# Для этого сначала следует конвертировать __COLOR_VARIANTS в нижний (или верхний) регистр.


# 2. Атрибуты owner, __model, __engine_power и __color следует явно задокументировать как атрибуты объекта,
# чтобы повысить читаемость кода.

# 3. Атрибут класса __COLOR_VARIANTS должен быть доступен внутри метода путем обращения через self.

# Пожалуйста, проверьте эти моменты и внесите соответствующие исправления.
# C уважением,
# Артём
