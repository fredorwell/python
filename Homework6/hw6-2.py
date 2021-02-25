# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина *
# масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода. Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.weigth = 25
        self.thickness = 5

    def mass(self):

        calculate = self.length * self.width * self.weigth * self.thickness / 1000
        print(f'Для строительства потребуется: {calculate} тонн')

road_to_village = Road(5000, 20)
road_to_village.mass()
