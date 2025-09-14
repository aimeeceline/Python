import math

'''1.Viết chương trình nhập vào một số nguyên n. Kiểm tra xem số đó có phải là số nguyên tố, số đối xứng,
số hoàn chỉnh, số chính phương hay không?'''
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

print("=== B.1: Kiểm tra 1 số n ===")
try:
    n = int(input("Nhập n: "))
    print(f"- {n} là số nguyên tố?        {'Có' if is_prime(n) else 'Không'}")
    print(f"- {n} là số đối xứng?         {'Có' if is_palindrome(n) else 'Không'}")
    print(f"- {n} là số hoàn chỉnh?       {'Có' if is_perfect(n) else 'Không'}")
    print(f"- {n} là số chính phương?     {'Có' if is_square(n) else 'Không'}")
except ValueError:
    print("⚠️ n phải là số nguyên.")
