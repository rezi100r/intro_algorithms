def bubble_sort(number, array):
    flag = True
    for index in range(number - 1):
        for j in range(number - index - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if flag:
            for x in array:
                print(x, end=' ')
            print('')
            flag = False


if __name__ == '__main__':
    number = int(input())
    array = [int(num) for num in input().split(' ')]
    bubble_sort(number, array)
