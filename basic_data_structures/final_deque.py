# ID проверки в контесте: 68740584

"""
Формат ввода
В первой строке записано количество команд n — целое число,
не превосходящее 100000. Во второй строке записано число m — максимальный
размер дека. Он не превосходит 50000. В следующих n строках записана
одна из команд:
    push_back(value) –  добавить элемент в конец дека. Если в деке уже
                        находится максимальное число элементов,
                        вывести «error».

    push_front(value) – добавить элемент в начало дека. Если в деке уже
                        находится максимальное число элементов,
                        вывести «error».

    pop_front() –       вывести первый элемент дека и удалить его.
                        Если дек был пуст, то вывести «error».

    pop_back() –        вывести последний элемент дека и удалить его.
                        Если дек был пуст, то вывести «error».

    Value —             целое число, по модулю не превосходящее 1000.

Формат вывода
Выведите результат выполнения каждой команды на отдельной строке.
Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.
"""
ERROR_MESSAGE = 'error'
ERROR_COMMAND = 'Error in command: {command}'


class Deque:
    def __init__(self, max_size):
        self.__items = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def __check_full_queue(self):
        return self.__size == self.__max_size

    def __check_empty_queue(self):
        return self.__size == 0

    def __get_index(self, method):
        if method == 'push_front':
            if self.__check_empty_queue():
                self.__head = 0
                self.__tail = 0
                return 0
            return (self.__head - 1) % self.__max_size
        if method == 'push_back':
            if self.__check_empty_queue():
                self.__head = 0
                self.__tail = 0
                return 0
            return (self.__tail + 1) % self.__max_size
        if method == 'pop_front':
            return (self.__head + 1) % self.__max_size
        if method == 'pop_back':
            return (self.__tail - 1) % self.__max_size

    def push_front(self, value):
        if self.__check_full_queue():
            raise RuntimeError(ERROR_MESSAGE)
        self.__head = self.__get_index('push_front')
        self.__items[self.__head] = value
        self.__size += 1

    def push_back(self, value):
        if self.__check_full_queue():
            raise RuntimeError(ERROR_MESSAGE)
        self.__tail = self.__get_index('push_back')
        self.__items[self.__tail] = value
        self.__size += 1

    def pop_front(self):
        if self.__check_empty_queue():
            raise RuntimeError(ERROR_MESSAGE)
        value = self.__items[self.__head]
        self.__head = self.__get_index('pop_front')
        self.__size -= 1
        return value

    def pop_back(self):
        if self.__check_empty_queue():
            raise RuntimeError(ERROR_MESSAGE)
        value = self.__items[self.__tail]
        self.__tail = self.__get_index('pop_back')
        self.__size -= 1
        return value


if __name__ == '__main__':
    command_count = int(input())
    deque = Deque(max_size=int(input()))
    for _ in range(command_count):
        try:
            command, *params = input().strip().split(' ')
            result = getattr(deque, command)(*params)
            if 'pop' in command:
                print(result)
        except RuntimeError:
            print(ERROR_MESSAGE)
        except AttributeError:
            raise ValueError(ERROR_COMMAND.format(command=command))
