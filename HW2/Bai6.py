# 6. Tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn [99;999] (tính cả 99 và 999)
def numbers_7_not_5_in_range():
    res = [x for x in range(99, 1000) if (x % 7 == 0 and x % 5 != 0)]
    return res

res = numbers_7_not_5_in_range()
print(res if res else "Không có")