class Depot:
    def __init__(self):
        pass

class OfficeEquipment:

    def __init__(self, name, serial_number, *args):
        self.name = name
        self.serial_number = serial_number

    def __str__(self):
        return f'название: {self.name} / серийный номер: {self.serial_number} /'

class Printer(OfficeEquipment):
    def __init__(self, name, serial_number, print_velocity):
        OfficeEquipment.__init__(self, name, serial_number)
        self.print_velocity = print_velocity

    def __str__(self):
        return f'Принтер: \n {OfficeEquipment.__str__(self)}' \
                f'Параметры: скорость печати {self.print_velocity} листов минуту'

class Scanner(OfficeEquipment):
    def __init__(self, name, serial_number, resolution):
        OfficeEquipment.__init__(self, name, serial_number)
        self.resolution = resolution

    def __str__(self):
        return f'Сканер: \n {OfficeEquipment.__str__(self)}' \
                f'Параметры: разрешающая способность {self.resolution} Мп'

class Copier(OfficeEquipment):
    def __init__(self, name, serial_number, addit):
        OfficeEquipment.__init__(self, name, serial_number)
        self.addit = addit

    def __str__(self):
        return f'Ксерокс: \n {OfficeEquipment.__str__(self)}' \
                f'Параметры: {self.addit} копии в минуту'

unit_1 = Printer('hp', 345678, 10)
unit_2 = Scanner('Canon', 984568, 10)
unit_3 = Copier('Xerox', 248567, 15)

print(unit_1)
print(unit_2)
print(unit_3)