# 5. In ra màn hình M số nguyên tố đầu tiên.
import math

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

def first_m_primes(M: int):
    if M <= 0:
        return []
    res, x = [], 2
    while len(res) < M:
        if is_prime(x):
            res.append(x)
        x += 1 if x == 2 else 2  # sau 2 chỉ xét số lẻ
    return res

try:
    M = int(input("Nhập M: ").strip())
    res = first_m_primes(M)
    print(res if res else "Không có")
except ValueError:
    print("⚠️ M phải là số nguyên.")
