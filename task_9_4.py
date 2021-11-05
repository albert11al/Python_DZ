from random import choice


class Car:

    def __init__(self, sp, co, na, po=False):
        self.speed = sp
        self.color = co
        self.name = na
        self.is_police = po

    def go(self):
        print(f'{self.name}: Сar went')

    def stop(self):
        print(f'{self.name}: Сar stopped')

    def turn(self):
        direction = ['налево', 'направо', 'назад']
        print(f'{self.name}: Car turned {choice(direction)}')

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}.'

class TownCar(Car):
    """ City car """

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 60 else super().show_speed()

class WorkCar(Car):
    """ Cargo truck """

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 40 else super().show_speed()

class SportCar(Car):
    """ Sports Car """

class PoliceCar(Car):
    """ Patrol car """

    def __init__(self, sp, co, na, po=True):
        super().__init__(sp, co, na, po=True)

police_car = PoliceCar(80, 'белый', '"Полицайка"')
work_car = WorkCar(40, 'хаки', '"Грузовичок"')
sport_car = SportCar(120, 'красный', '"Спортивка"')
town_car = TownCar(60, 'жёлтый', '"Малютка"')

list_of_cars = [police_car, work_car, sport_car, town_car]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()


