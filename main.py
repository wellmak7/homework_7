class Matrix:

    def __init__(self, list_1, list_2, list_3):
        self.list_1 = list_1
        self.list_2 = list_2
        self.list_3 = list_3

    def __str__(self):
        return f'{self.list_1}\n' \
               f'{self.list_2}\n' \
               f'{self.list_3}'

    def __add__(self, other):
        new_list_1 = []
        new_list_2 = []
        new_list_3 = []

        for i in range(0, len(self.list_1)):
            new_el = self.list_1[i] + other.list_1[i]
            new_list_1.append(new_el)

        for i in range(0, len(self.list_2)):
            new_el = self.list_2[i] + other.list_2[i]
            new_list_2.append(new_el)

        for i in range(0, len(self.list_3)):
            new_el = self.list_3[i] + other.list_3[i]
            new_list_3.append(new_el)

        return Matrix(new_list_1, new_list_2, new_list_3)

matrix_1 = Matrix([2,5,1],[7,5,9],[8,9,0])
matrix_2 = Matrix([2, 5, 1], [7, 5, 9], [8, 9, 0])

print(matrix_1)
print(matrix_1 + matrix_2)