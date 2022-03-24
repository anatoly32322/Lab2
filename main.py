import half_division
import simple_iteration
import newton
import matplotlib.pyplot as plt
import numpy as np


def main():
    equation_type = input('Какой тип уравнений вы хотите решить: СНУ (+) или нелинейное уравнение (-)\n')
    if equation_type == '+':
        print('Будет выполнено решение следующей СНУ:')
        print('x^3 + 2x^2 + 3x = y')
        print('x^3 + y^3 = 10')
        functionF = lambda x, y: pow(x, 3) + 2 * pow(x, 2) + 3 * x - y
        functionG = lambda x, y: pow(x, 3) + pow(y, 3) - 10
        plot_system(functionF, functionG)
        left_border, right_border = read_borders()
        epsilon = float(input('Введите погрешность вычисления решения: \n'))
        newton_solver = newton.Newton(left_border, right_border, epsilon, functionF, functionG)
        newton_solver.solve()
    else:
        print('Вам на выбор дано 3 уравнения. Выберете то, которое хотите решить:')
        print('1. 2.74 * x^3 - 1.93 * x^2 - 15.28 * x - 3.72')
        print('2. -1.38 * x^3 - 5.42 * x^2 + 2.57 * x + 10.95')
        print('3. cos(x) + x')
        which_func = input('Введите номер фукнции, которую хотите решить:\n')
        f, phi = get_func(which_func)
        plot_equation(f)
        left_border, right_border = read_borders()
        epsilon = float(input('Введите погрешность вычисления решения: \n'))
        print("Записать ответ в файл (-) или вывести в консоль (+)?")
        type_write = input()
        halfDivision_solver = half_division.HalfDivision(left_border, right_border, epsilon, f)
        halfDivision_solver.solve()
        simpleIteration_solver = simple_iteration.SimpleIteration(left_border, right_border, epsilon, f, phi)
        simpleIteration_solver.solve()


def get_func(which_func):
    if which_func == '1':
        return lambda x: 2.74 * pow(x, 3) - 1.93 * pow(x, 2) - 15.28 * x - 3.72, \
            lambda x: pow((1.93 * pow(x, 2) + 15.28 * x + 3.72) / 2.74, 1/3)
    elif which_func == '2':
        return lambda x: -1.38 * pow(x, 3) - 5.42 * pow(x, 2) + 2.57 * x + 10.95, \
            lambda x: pow((5.42 * pow(x, 2) - 2.57 * x - 10.95) / -1.38, 1/3)
    else:
        return lambda x: np.cos(x) + x, \
            lambda x: -np.cos(x)


def read_borders():
    left_border = float(input('Введите левую границу поиска решения: \n'))
    right_border = float(input('Введите правую границу поиска решения: \n'))
    return left_border, right_border

def plot_system(f, g):
    plt.gcf().canvas.manager.set_window_title("График функции")
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.plot(1, 0, marker=">", ms=5, color='k',
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, marker="^", ms=5, color='k',
            transform=ax.get_xaxis_transform(), clip_on=False)
    xRange = np.arange(-10, 10, 0.025)
    yRange = np.arange(-10, 10, 0.025)
    X, Y = np.meshgrid(xRange, yRange)
    F = f(X, Y)
    G = g(X, Y)
    plt.contour(X, Y, F, [0])
    plt.contour(X, Y, G, [0])
    plt.show()


def plot_equation(f):
    plt.gcf().canvas.manager.set_window_title("График функции")
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.plot(1, 0, marker=">", ms=5, color='k',
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, marker="^", ms=5, color='k',
            transform=ax.get_xaxis_transform(), clip_on=False)
    xRange = np.arange(-10, 10, 0.025)
    yRange = np.arange(-10, 10, 0.025)
    X, Y = np.meshgrid(xRange, yRange)
    F = f(X)
    plt.contour(X, Y, F, [0])
    plt.show()


if __name__ == '__main__':
    main()
