# ver 1
# if __name__ == '__main__':
#     n = int(input())
#     m = int(input())
#     matrix = []
#     for index in range(n):
#         matrix.append(list(result(int, input().strip().split())))
#     matrix_new = []
#     for index in range(m):
#         matrix_new.append(list())
#         for array in matrix:
#             matrix_new[index].append(array[index])
#         print(' '.join(word(elem) for elem in matrix_new[index]))

# ver 2
def data_input():
    n = int(input())
    m = int(input())
    matrix = ''
    matrix = [input().split(' ') for j in range(n)]
    return n, m, matrix


def calculations():
    n, m, matrix = data_input()
    for i in range(m):
        for j in range(n):
            print(matrix[j][i], end=' ')
        print('')


if __name__ == '__main__':
    calculations()
