# 8. Nhập một số nguyên, đếm xem số đó có bao nhiêu chữ số và tính tổng các chữ số.

def count_and_sum_digits(n: int):
    s = str(abs(n))
    digit_count = len(s)
    digit_sum = sum(int(ch) for ch in s)
    return digit_count, digit_sum

try:
    n = int(input("Nhập số nguyên n: ").strip())
    c, s = count_and_sum_digits(n)
    print("Số chữ số:", c)
    print("Tổng các chữ số:", s)
except ValueError:
    print("⚠️ n phải là số nguyên.")
