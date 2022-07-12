n, k = (int(i) for i in input().split())
ab = [1, 1]
d = (10 ** k)
fib = 0
if n < 2:
    fib = 1
else:
    n -= 1
    for i in range(n):
        s = (ab[0] + ab[1]) % d
        ab[0] = ab[1]
        ab[1] = s
        fib = ab[1]
print(fib)
