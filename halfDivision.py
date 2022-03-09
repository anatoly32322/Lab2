from function import func


class HalfDivision:
    __l = None
    __r = None
    __eps = None
    __ans = None
    __counter = 0

    def __init__(self, l, r, eps):
        self.__l = l
        self.__r = r
        self.__eps = eps

    def solve(self):
        if not self.__check_solution():
            return False
        self.__find_solution()
        self.__calc_answer()
        self.__print_answer()

    def __calc_answer(self):
        self.__ans = (self.__l + self.__r) / 2

    def __print_answer(self):
        print('Ответ: {}'.format(self.__ans))
        print('Результат функции: {}'.format(func(self.__ans)))
        print('Количество итераций для получения ответа с заданной точностью: {}'.format(self.__counter))

    def __find_solution(self):
        while self.__r - self.__l > self.__eps:
            m = (self.__r + self.__l) / 2
            if func(m) * func(self.__l) < 0:
                self.__r = m
            else:
                self.__l = m
            self.__counter += 1

    def __check_solution(self):
        if func(self.__l) * func(self.__r) <= 0:
            return True
        return False
