class Cell:

    def __init__(self, cells_amount):
        self.cells_amount = cells_amount

    def __add__(self, other):
        return self.cells_amount + other.cells_amount

    def __sub__(self, other):
        if self.cells_amount - other.cells_amount > 0:
            return self.cells_amount - other.cells_amount
        else:
            print("Разность количества ячеек не больше нуля!")

    def __mul__(self, other):
        return self.cells_amount * other.cells_amount

    def __truediv__(self, other):
        return round(self.cells_amount / other.cells_amount)

    def make_order(self, cells_per_row):
        self.cells_per_row = cells_per_row
        self.rows = self.cells_amount // self.cells_per_row

        print("Организация ячеек по рядам: ")

        for i in range(0, self.rows):
            for j in range(0, self.cells_per_row):
                print(f'*', end = '')
            print("\n")

        for z in range(0, self.cells_amount - self.rows * self.cells_per_row):
            print(f'*', end='')

        print()


cell_1 = Cell(12)
cell_2 = Cell(11)

print("Сложение клеток: ", cell_1 + cell_2)
print("Вычитание клеток: ", cell_1 - cell_2)
print("Умножение клеток: ", cell_1 * cell_2)
print("Деление клеток: ", cell_1 / cell_2)

cell_1.make_order(5)