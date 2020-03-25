from copy import copy
from math import sqrt


"""
SOLUTION #2 (OOP style)
"""


class QuadraticEquation:
    def __init__(self, a, b, c):
        self.A = float(a)
        self.B = float(b)
        self.C = float(c)
        self.D = None
        self.X_1 = None
        self.X_2 = None

    def __calculate_discriminant(self):
        """Вычисление дискриминанта"""

        self.D = self.B**2 - 4 * self.A * self.C

    def __calculate_radicals(self):
        """Вычисление корней"""

        if self.D > 0:
            # сортирую для вывода корней по возрастанию
            radicals = sorted([(-self.B + sqrt(self.D))/(2*self.A), (-self.B - sqrt(self.D)) / (2 * self.A)])
            self.X_1 = radicals[0]
            self.X_2 = radicals[1]
        elif self.D == 0:
            self.X_1 = -self.B/(2*self.A)
            self.X_2 = copy(self.X_1)

    def show_solution(self):
        """Вывод ответа"""

        self.__calculate_discriminant()
        self.__calculate_radicals()

        if not self.X_1:
            print('Нет действительных корней')
        else:
            print(self.X_1, self.X_2)


equation = QuadraticEquation(input(), input(), input())
equation.show_solution()
