# ID проверки в контесте: 68857924
"""
Формат ввода
Функция принимает массив натуральных чисел и искомое число
k. Длина массива не превосходит 10000. Элементы массива и число k не
превосходят по значению 10000.
В примерах:
В первой строке записано число n –— длина массива.
Во второй строке записано положительное число k –— искомый элемент.
Далее в строку через пробел записано n натуральных чисел – элементы массива.

Формат вывода
Функция должна вернуть индекс элемента, равного k, если такой есть в
массиве (нумерация с нуля). Если элемент не найден, функция должна
вернуть −1.
Изменять массив нельзя.
Для отсечения неэффективных решений ваша функция будет запускаться
от 100000 до 1000000 раз.
Пример
Ввод:
9
5
19 21 100 101 1 4 5 7 12
Вывод:
6
"""


def broken_search(nums: list, target: int) -> int:
    start_idx = 0
    end_idx = len(nums) - 1
    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        if nums[mid_idx] == target:
            return mid_idx
        elif nums[start_idx] <= nums[mid_idx]:
            if nums[start_idx] <= target < nums[mid_idx]:
                end_idx = mid_idx - 1
            else:
                start_idx = mid_idx + 1
        else:
            if nums[mid_idx] < target <= nums[end_idx]:
                start_idx = mid_idx + 1
            else:
                end_idx = mid_idx - 1
    return -1


if __name__ == '__main__':
    count_array = int(input())
    target_number = int(input())
    numbers_array = [int(num) for num in input().split()]

    print(broken_search(numbers_array, target_number))
