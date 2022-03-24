class SimpleIteration:
    __l = None
    __r = None
    __eps = None
    __ans = None
    __counter = 0
    __f = None
    __phi = None
    __type_write = None

    def __init__(self, l, r, eps, f, phi, type_write):
        self.__l = l
        self.__r = r
        self.__eps = eps
        self.__f = f
        self.__phi = phi
        self.__type_write = type_write

    def solve(self):
        x = self.__l
        x0 = float('inf')
        while abs(x - x0) > self.__eps:
            x0 = x
            x = self.__phi(x0)
            self.__counter += 1
        self.__ans = x
        self.__print_answer()

    def __print_answer(self):
        if self.__type_write == '+':
            print('Метод простой итерации:')
            print('Ответ: {}'.format(self.__ans))
            print('Результат функции: {}'.format(self.__f(self.__ans)))
            print('Количество итераций для получения ответа с заданной точностью: {}'.format(self.__counter))
            print('_________________________________________')
        else:
            with open('output.txt', 'w', encoding='utf-8') as f:
                f.write('Метод простой итерации:\n' +
                        f'Ответ: {self.__ans}\n' +
                        f'Результат функции: {self.__f(self.__ans)}\n' +
                        f'Количество итераций для получения ответа с заданной точностью: {self.__counter}\n' +
                        '_________________________________________\n')
