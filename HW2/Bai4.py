# 4. Liệt kê tất cả các số nguyên tố nhỏ hơn N ( N nhập từ bàn phím)
import math

def primes_less_than(N: int):
    if N <= 2:
        return []
    sieve = [True] * N
    sieve[0] = sieve[1] = False
    limit = int(math.isqrt(N))
    for p in range(2, limit + 1):
        if sieve[p]:
            start = p * p
            sieve[start:N:p] = [False] * len(range(start, N, p))
    return [i for i, ok in enumerate(sieve) if ok]


try:
    N = int(input("Nhập N: "))
    res = primes_less_than(N)
    print(res if res else "Không có")
except ValueError:
    print("⚠️ N phải là số nguyên.")
