
import math
from typing import List, Tuple
'''2. Viết chương trình nhập vào hai số M, N. In ra tất cả các số nguyên tố, số đối xứng, số hoàn chỉnh, số
chính phương trong khoảng [M,N] (nếu có)'''

import math
from typing import List, Tuple
'''2. Viết chương trình nhập vào hai số M, N. In ra tất cả các số nguyên tố, số đối xứng, số hoàn chỉnh, số
chính phương trong khoảng [M,N] (nếu có)'''
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for d in range(3, r + 1, 2):
        if n % d == 0:
            return False
    return True

def is_palindrome(n: int) -> bool:
    s = str(abs(n))
    return s == s[::-1]

def is_perfect(n: int) -> bool:
    if n <= 1:
        return False
    total = 1
    r = int(math.isqrt(n))
    for d in range(2, r + 1):
        if n % d == 0:
            total += d
            q = n // d
            if q != d:
                total += q
    return total == n

def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n

def list_in_range(M: int, N: int) -> Tuple[List[int], List[int], List[int], List[int]]:
    if M > N:
        M, N = N, M
    primes = []
    pals = []
    perfects = []
    squares = []
    for x in range(min(M, N) + 1, max(M, N)):
        if is_prime(x):
            primes.append(x)
        if is_palindrome(x):
            pals.append(x)
        if is_perfect(x):
            perfects.append(x)
        if is_square(x):
            squares.append(x)
    return primes, pals, perfects, squares

def primes_less_than(N: int) -> List[int]:
    if N <= 2:
        return []
    sieve = [True] * N
    sieve[0] = sieve[1] = False
    limit = int(math.isqrt(N))
    for p in range(2, limit + 1):
        if sieve[p]:
            step_start = p * p
            sieve[step_start:N:p] = [False] * len(range(step_start, N, p))
    return [i for i, ok in enumerate(sieve) if ok]

def first_m_primes(M: int) -> List[int]:
    res = []
    x = 2
    while len(res) < M:
        if is_prime(x):
            res.append(x)
        x += 1 if x == 2 else 2  # sau 2 chỉ xét số lẻ
    return res

print("=== B.2: Liệt kê trong khoảng [M, N] ===")
try:
    M = int(input("Nhập M: "))
    N = int(input("Nhập N: "))
    primes, pals, perfects, squares = list_in_range(M, N)
    print(f"- Số nguyên tố trong [{min(M,N)}, {max(M,N)}]: {primes if primes else 'Không có'}")
    print(f"- Số đối xứng trong [{min(M,N)}, {max(M,N)}]: {pals if pals else 'Không có'}")
    print(f"- Số hoàn chỉnh trong [{min(M,N)}, {max(M,N)}]: {perfects if perfects else 'Không có'}")
    print(f"- Số chính phương trong [{min(M,N)}, {max(M,N)}]: {squares if squares else 'Không có'}")
except ValueError:
    print("⚠️ M, N phải là số nguyên.")

