def flowerbed():
    count_line = int(input())
    flower_mans = [None] * count_line
    for i in range(count_line):
        start, end = map(int, input().split())
        flower_mans[i] = [start, end]

    flower_mans.sort()
    results = []
    idx = 0
    big_start, big_end = flower_mans[idx]
    idx += 1
    while idx < count_line:
        if big_start <= flower_mans[idx][0] <= big_end:
            _, curr_end = flower_mans[idx]
            idx += 1
            if curr_end > big_end:
                big_end = curr_end
        else:
            results.append([big_start, big_end])
            big_start, big_end = flower_mans[idx]
            idx += 1
    results.append([big_start, big_end])

    for res in results:
        print(*res)


if __name__ == '__main__':
    flowerbed()
