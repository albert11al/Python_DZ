class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join(map(str, self.my_list))

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)

matrix_1 = Matrix([[5, 3, 1], [4, 4, 4], [9, 0, 5]])
matrix_2 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(f'Matrix 1\n{matrix_1}\n{"-" * 20}')
print(f'Matrix 2\n{matrix_2}\n{"-" * 20}')
print(f'matrix 1 + matrix 2\n{matrix_1 + matrix_2}')