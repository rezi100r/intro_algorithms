# ID успешной посылки 68381073
from typing import List, Tuple


def trainer(number: int, matrix: List[str]) -> int:
    numbers = {a: 0 for a in range(1, 10)}
    scores = 0
    for i in range(4):
        for k in matrix[i]:
            if k == '.':
                continue
            numbers[int(k)] += 1
    for i in numbers.values():
        if 0 < i <= 2 * number:
            scores += 1
    return scores


def read_input() -> Tuple[int, List[str]]:
    number = int(input())
    matrix = [str(input()) for i in range(4)]
    return number, matrix


if __name__ == '__main__':
    number, matrix = read_input()
    print(trainer(number, matrix))
