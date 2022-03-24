class HalfDivision:
    __l = None
    __r = None
    __eps = None
    __ans = None
    __counter = 0
    __f = None
    __type_write = None

    def __init__(self, l, r, eps, f, type_write):
        self.__l = l
        self.__r = r
        self.__eps = eps
        self.__f = f
        self.__type_write = type_write

    def solve(self):
        if not self.__check_solution():
            return False
        self.__find_solution()
        self.__calc_answer()
        self.__print_answer()

    def __calc_answer(self):
        self.__ans = (self.__l + self.__r) / 2

    def __print_answer(self):
        if self.__type_write == '+':
            print('Метод половинного деления:')
            print('Ответ: {}'.format(self.__ans))
            print('Результат функции: {}'.format(self.__f(self.__ans)))
            print('Количество итераций для получения ответа с заданной точностью: {}'.format(self.__counter))
            print('_________________________________________')
        else:
            with open('output.txt', 'w', encoding='utf-8') as f:
                f.write('Метод половинного деления:\n' +
                        f'Ответ: {self.__ans}\n' +
                        f'Результат функции: {self.__f(self.__ans)}\n' +
                        f'Количество итераций для получения ответа с заданной точностью: {self.__counter}\n' +
                        '_________________________________________\n')

    def __find_solution(self):
        while self.__r - self.__l > self.__eps:
            m = (self.__r + self.__l) / 2
            if self.__f(m) * self.__f(self.__l) < 0:
                self.__r = m
            else:
                self.__l = m
            self.__counter += 1

    def __check_solution(self):
        if self.__f(self.__l) * self.__f(self.__r) <= 0:
            return True
        return False
