# 7. Tìm số đầu tiên chia hết cho 9 và chia hết cho 7 nằm trong đoạn [M,N]

def first_divisible_by_63(M: int, N: int):
    if M > N:
        M, N = N, M
    step = 63
    # tìm bội đầu tiên của 63 ≥ M
    k = (M + step - 1) // step  # ceil(M/63) nhưng dùng số nguyên
    candidate = k * step
    return candidate if candidate <= N else None

try:
    M = int(input("Nhập M: ").strip())
    N = int(input("Nhập N: ").strip())
    ans = first_divisible_by_63(M, N)
    print(ans if ans is not None else "Không có")
except ValueError:
    print("⚠️ M, N phải là số nguyên.")
