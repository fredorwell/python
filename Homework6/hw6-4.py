# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево).
#
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed.
#
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехал.'

    def stop(self):
        return f'\n{self.name} остановился.'

    def turn(self, direction):
        return f'\n{self.name} повернул {direction}'

    def show_speed(self):
        return f'\nВаша скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВы привышаете скорость, разрешенная скорость - {self.speed}'
        else:
            return f'Ваша скорость - {self.name}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВы привышаете скорость, разрешенная скорость - {self.speed}'
        else:
            return f'Ваша скорость - {self.name}'


class PoliceCar(Car):
    pass


town = TownCar('городской автомобиль', 70, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('направо'), town.turn('налево'), town.stop())

sport = SportCar('спортивный автомобиль', 170, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('служебный автомобиль', 30, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())
