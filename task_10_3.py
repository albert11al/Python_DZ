class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, row):
        result = ''
        for i in range(int(self.nums // row)):
            result += '@_@ ' * row + '\n' + '$_$ ' * (self.nums % row)
        return result

    def __add__(self, other):
        return f'сумма клеток: {self.nums + other.nums}'

    def __sub__(self, other):
        return f'вычитание клеток: {self.nums - other.nums}' \
            if (self.nums - other.nums) > 0 else 'Клетка исчезла :('

    def __mul__(self, other):
        return f'количество клеток: {self.nums * other.nums}'

    def __floordiv__(self, other):
        return f'целочисленное деление двух клеток: {self.nums // other.nums}'

cell_1 = Cell(10)
cell_2 = Cell(7)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(4))