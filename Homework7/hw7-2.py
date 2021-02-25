# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий
# подсчет расхода ткани.

# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для
# основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class tiss_cons(ABC):
    def __init__(self, input_data):
        self.param = input_data

    @abstractmethod
    def calculate(self):
        pass


class coat_cons(tiss_cons):
    @property
    def calculate(self):
        res = round(self.param / 6.5 + 0.5)
        return f'На пальто потребуется {res} ткани'


class suit_cons(tiss_cons):
    @property
    def calculate(self):
        res = round(2 * self.param + 0.3)
        return f'На костюм потребуется {res} ткани'


coat_size = coat_cons(10)
suit_heig = suit_cons(10)
print(coat_size.calculate)
print(suit_heig.calculate)