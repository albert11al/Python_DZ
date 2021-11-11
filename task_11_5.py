from datetime import datetime

class Depot:
    def __init__(self, name):
        self.name = name
        self.lists = {}
        self.give_lists = {}

    def take_to_depot(self, equipment):
# внесение в словарь название оборудования, серийный номер и время передачи на склад
        t = datetime.now()
        self.lists.update({equipment.serial_number: [equipment.name, self, equipment.quantity, t]})
        return f'На склад {self.name} получено оборудование: {equipment.name}, количество: {equipment.quantity}, серийный номер - {equipment.serial_number}, ' \
               f'Дата: {t.day}. {t.month}. {t.year}'

    def give_to_depot(self, equipment, other):
# передача оборудование на другой склад или подразделение
        t = datetime.now()
        self.give_lists.update({equipment.serial_number: [equipment.name, other, t]})
        other.take_to_depot(equipment)
        return f'На склад {self.name}, передано оборудование: {equipment.name}, серийный номер - {equipment.serial_number}, ' \
               f'Дата: {t.day}. {t.month}. {t.year}'


    def list_equipments(self):
        print('На склад ' + self.name + ' получено оборудование:')
        print(self.lists)
        print('Общее количество: ', len(self.lists))
        print('Со склада ' + self.name + ' выдано оборудование:')
        print(self.give_lists)
        print('Общее количество: ', len(self.give_lists))

class OfficeEquipment:

    def __init__(self, name, serial_number, quantity, *args):
        self.name = name
        self.serial_number = serial_number
        self.quantity = quantity

    def __str__(self):
        return f'название: {self.name} / серийный номер: {self.serial_number} / количество: {self.quantity} /'

class Printer(OfficeEquipment):
    def __init__(self, name, serial_number, quantity, print_velocity):
        OfficeEquipment.__init__(self, name, serial_number, quantity)
        self.print_velocity = print_velocity

    def __str__(self):
        return f'Принтер: \n {OfficeEquipment.__str__(self)}' \
                f'Параметры: скорость печати {self.print_velocity} листов минуту'

class Scanner(OfficeEquipment):
    def __init__(self, name, serial_number, quantity, resolution):
        OfficeEquipment.__init__(self, name, serial_number, quantity)
        self.resolution = resolution

    def __str__(self):
        return f'Сканер: \n {OfficeEquipment.__str__(self)}' \
                f'Параметры: разрешающая способность {self.resolution} Мп'

class Copier(OfficeEquipment):
    def __init__(self, name, serial_number, quantity, addit):
        OfficeEquipment.__init__(self, name, serial_number, quantity)
        self.addit = addit

    def __str__(self):
        return f'Ксерокс: \n {OfficeEquipment.__str__(self)}' \
                f'Параметры: {self.addit} копии в минуту'

store1 = Depot('Main warehouse')
store2 = Depot('Small warehouse')
unit_1 = Printer('hp', 345678, 4, 10)
unit_2 = Scanner('Canon', 984568, 3, 10)
unit_3 = Copier('Xerox', 248567, 1, 15)

print(unit_1)
print(unit_2)
print(unit_3)

print(store1.take_to_depot(unit_1))
print(store1.take_to_depot(unit_2))
print(store1.take_to_depot(unit_3))

store1.give_to_depot(unit_1, store2)

store1.list_equipments()
store2.list_equipments()
