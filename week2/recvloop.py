import timeit

def fac_iter(n):
    fac = 1
    for i in range(2, n + 1):
        fac *= i
    return fac

def fac_rec(n):
    if n <= 1:
        return 1
    return n * fac_rec(n - 1)

print(timeit.timeit("fac_iter(1000)", globals=globals(), number=1_000_000))
print(timeit.timeit("fac_rec(1000)", globals=globals(), number=1_000_000))
