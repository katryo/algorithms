from math import sqrt
from math import floor


def sieve(n):
    end = floor(sqrt(n))
    for i in range(2, n+1):
        failed = False
        for j in range(2, min(end+1, i)):
            if i % j == 0:
                failed = True
                continue
        if not failed:
            yield i


print(list(sieve(10000)))
