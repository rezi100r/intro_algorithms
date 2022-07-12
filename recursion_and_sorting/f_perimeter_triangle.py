def sort_find(array):
    for index in range(0, len(array) - 1):
        if array[index] < (array[index + 1] + array[index + 2]):
            return array[index] + array[index + 1] + array[index + 2]


if __name__ == '__main__':
    _ = int(input())
    array = [int(num) for num in input().split(' ')]
    print(sort_find(sorted(array, reverse=True)))
