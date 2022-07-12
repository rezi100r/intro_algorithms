"""
Двоичная система

Тимофей записал два числа в двоичной системе счисления и попросил Гошу 
вывести их сумму, также в двоичной системе. Встроенную в язык 
программирования возможность сложения двоичных чисел применять нельзя. 
Помогите Гоше решить задачу.

Решение должно работать за O(N), где N –— количество разрядов максимального 
числа на входе.

Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке. 
Длина каждого числа не превосходит 10 000 символов.

Формат вывода
Одно число в двоичной системе счисления.

Пример 1
Ввод	            Вывод
1010                10101
1011
"""

from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    first_number = list(first_number[::-1])
    second_number = list(second_number[::-1])
    first_number = list(map(int, first_number))
    second_number = list(map(int, second_number))
    max_size = max(len(first_number), len(second_number))
    first_number += [0] * (max_size - len(first_number))
    second_number += [0] * (max_size - len(second_number))
    overflow = 0
    result = []
    for obj in zip(first_number, second_number):
        value = obj[0] + obj[1] + overflow
        overflow = value // 2
        result.append(value % 2)
    if overflow == 1:
        result.append(1)
    result = result[::-1]
    return ''.join(map(str, result))


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
