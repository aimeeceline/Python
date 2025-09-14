def gcd_iter(a: int, b: int) -> int:
    """Ước chung lớn nhất (GCD) không dùng đệ quy."""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def lcm_iter(a: int, b: int) -> int:
    """Bội số chung nhỏ nhất (LCM) dùng GCD không đệ quy."""
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd_iter(a, b) * b)

def gcd_rec(a: int, b: int) -> int:
    """Ước chung lớn nhất (GCD) dùng đệ quy."""
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_rec(b, a % b)

def lcm_rec(a: int, b: int) -> int:
    """Bội số chung nhỏ nhất (LCM) dùng GCD đệ quy."""
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd_rec(a, b) * b)

try:
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))

    print("=== Không đệ quy ===")
    print(f"GCD(a,b) = {gcd_iter(a,b)}")
    print(f"LCM(a,b) = {lcm_iter(a,b)}")

    print("=== Đệ quy ===")
    print(f"GCD(a,b) = {gcd_rec(a,b)}")
    print(f"LCM(a,b) = {lcm_rec(a,b)}")

except ValueError:
    print("⚠️ a, b phải là số nguyên.")
