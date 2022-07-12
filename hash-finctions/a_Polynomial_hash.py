def hash_string(a, m, istring):
    tmp = ord(istring[-1])
    lenght = a
    for c in istring[-2::-1]:
        tmp = (tmp + ord(c) * lenght)
        lenght = (lenght * a) % m
    print(tmp % m)


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    input_string = input()
    if input_string == '':
        print(0)
    else:
        hash_string(a, m, input_string)