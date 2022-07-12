# ID проверки в контесте: 68883090
"""
Формат ввода
В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
В каждой из следующих n строк задана информация про одного из участников.
i-й участник описывается тремя параметрами:

уникальным логином (строкой из маленьких латинских букв длиной не более 20)
числом решённых задач Pi штрафом Fi
Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109 (10 ** 9).

Формат вывода
Для отсортированного списка участников выведите по порядку их логины по
одному в строке.

Пример
Ввод:           Вывод:
5
alla 4 100      gena
gena 6 1000     timofey
gosha 2 90      alla
rita 2 90       gosha
timofey 4 80    rita
"""


class Participant:
    def __init__(self, name, points, penalty):
        self.name = name
        self.points = points
        self.penalty = penalty

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if isinstance(other, Participant):
            return(
                (-self.points, self.penalty, self.name) <
                (-other.points, other.penalty, other.name)
            )
        return NotImplemented


def quicksort(array: list, start=0, end=0):

    def _partition(low, high):
        if low >= high:
            return
        left = low
        right = high
        pivot = array[(right + left) // 2]
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _partition(low, right)
        _partition(left, high)

    _partition(start, end - 1)


if __name__ == '__main__':
    number = int(input())
    players = []
    for index in range(number):
        name, points, penalty = input().split()
        players.append(
            Participant(points=int(points), penalty=int(penalty), name=name)
        )
    quicksort(players, end=len(players))
    print(*players, sep='\n')
