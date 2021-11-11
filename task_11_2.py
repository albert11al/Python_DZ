class DivisionByNull:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def divide_by_null(numerator, denominator):
        try:
            return (numerator / denominator)
        except:
            return (f"Деление на ноль недопустимо")



a = int(input('введи числитель: '))
b = int(input('введи знаменатель: '))
print(DivisionByNull.divide_by_null(a, b))
