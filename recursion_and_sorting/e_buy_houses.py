def how_many(budget, cost):
    if len(cost) > 1:
        cost = sorted(cost)
    count = 0
    for house in cost:
        budget -= house
        if budget >= 0:
            count += 1
        else:
            return count
    return count


if __name__ == '__main__':
    num, budget = map(int, input().split())
    houses_cost = list(map(int, input().split()))
    print(how_many(budget, houses_cost))
