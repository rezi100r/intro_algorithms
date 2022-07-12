# ID успешной посылки 68380657
from typing import List, Tuple


def calculate(numbers: List[int], length: int) -> List[int]:
    distance = []
    zero_position = None
    for i, value in enumerate(numbers):
        if value == 0:
            zero_position = i
            distance.append(0)
            continue
        if zero_position is not None:
            distance.append(i - zero_position)
        else:
            distance.append(length)
    return distance


def nearest_zero(length: int, number_street: List[int]) -> List[int]:
    distance = calculate(number_street, length)
    r_distance = (calculate(number_street[::-1], length))[::-1]
    result = []
    for step in range(length):
        result.append(min(distance[step], r_distance[step]))
    return result


def read_input() -> Tuple[int, List[int]]:
    length = int(input())
    number_street = [int(num) for num in input().split(' ')]
    return length, number_street


if __name__ == '__main__':
    length, number_street = read_input()
    print(' '.join([str(x) for x in nearest_zero(length, number_street)]))
