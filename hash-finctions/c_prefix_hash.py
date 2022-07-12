def calc(a, m, length):
    result = [1, ]
    for c in range(0, length):
        result.append(result[c] * a % m)
    return result


def find_hash(m, word, prefix):
    result = 0
    count = 0
    for c in word[::-1]:
        result = (result + ord(c) * prefix[count])
        count += 1
    return result % m


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    input_string = input()
    prefix = calc(a, m, (len(input_string) - 1))
    for i in range(int(input())):
        left, right = input().split()
        print(find_hash(
            m,
            input_string[int(left) - 1:int(right)],
            prefix
        ))
