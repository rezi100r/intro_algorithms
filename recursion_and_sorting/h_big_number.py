def comparate(num1, num2):
    return num1 < num2


def insertion_sort(array, less):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and less(int(array[j] + key_item), int(key_item + array[j])):
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1
    print(''.join(array))


if __name__ == '__main__':
    number = int(input())
    source_array = input().split(' ')
    insertion_sort(source_array, comparate)
