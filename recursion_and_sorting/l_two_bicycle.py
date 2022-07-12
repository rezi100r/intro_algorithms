def binary_search_bicycle(money, price, left, right):
    if right <= left != 0:
        return -1
    mid = (left + right) // 2
    if money[mid] >= price > money[mid - 1] or mid == 0:
        return mid + 1
    elif price <= money[mid]:
        return binary_search_bicycle(money, price, left, mid)
    else:
        return binary_search_bicycle(money, price, mid + 1, right)


# def read_input():
#     days = int(input())
#     money = [int(num) for num in input().split(' ')]
#     price = int(input())
#     return money, price


# if __name__ == '__main__':
days = int(input())
money = [int(num) for num in input().split(' ')]
price = int(input())
print(binary_search_bicycle(
    money,
    price,
    left=0,
    right=len(money)),
    end=' '
)
print(binary_search_bicycle(
    money,
    price * 2,
    left=0,
    right=len(money)),
    end=' '
)
