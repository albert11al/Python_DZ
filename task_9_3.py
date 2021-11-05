class Worker:
    def __init__(self, na, su, po, wage, bonus):
        self.name = na
        self.surname = su
        self.position = po
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'сотрудник: {self.position} {self.name} {self.surname}.'
    def get_total_income(self):
        return f' получает ЗП: {sum(self._income.values())}'

worker = Position("Ivan", "Ivanov", "IT", 43000, 21000)
print(worker.get_full_name() + worker.get_total_income())


