from collections import defaultdict


def prime_factorization(n):
    ans = defaultdict(int)
    factor = 2
    while n > 1:
        while n % factor == 0:
            n //= factor
            ans[factor] += 1
        factor += 1
    return ans


print(prime_factorization(100))
print(prime_factorization(264))
print(prime_factorization(373))
print(prime_factorization(400))
