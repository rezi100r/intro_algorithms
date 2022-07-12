# ID проверки в контесте: 68741155
"""
Формат ввода
В единственной строке дано выражение, записанное в обратной польской нотации.
Числа и арифметические операции записаны через пробел.
На вход могут подаваться операции: +, -, *, / и числа, по модулю не
превосходящие 10000. Гарантируется, что значение промежуточных выражений в
тестовых данных по модулю не больше 50000.

Формат вывода
Выведите единственное число — значение выражения.
"""


OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        try:
            return self.__items.pop()
        except IndexError:
            raise IndexError('Нет операндов для расчета.')


def calculator(line):
    stack = Stack()
    for element in line:
        if element in OPERATORS:
            operand1, operand2 = stack.pop(), stack.pop()
            try:
                stack.push(int(OPERATORS[element](operand2, operand1)))
            except ZeroDivisionError:
                raise ZeroDivisionError('Ошибка деления на ноль.')
            except TypeError:
                raise TypeError(f'{element} операция не поддерживается.')
        else:
            try:
                stack.push(int(element))
            except:
                raise KeyError(f'Невозможно преобразовать {element}')
    return stack.pop()


if __name__ == '__main__':
    inp_string = input().split()
    print(calculator(inp_string))
