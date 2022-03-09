import halfDivision


def main():
    left_border = float(input('Введите левую границу поиска решения: \n'))
    right_border = float(input('Введите правую границу поиска решения: \n'))
    epsilon = float(input('Введите погрешность вычисления решения: \n'))
    solver = halfDivision.HalfDivision(left_border, right_border, epsilon)
    solver.solve()


if __name__ == '__main__':
    main()
