# Viết chương trình nhập số A và kiểm tra xem A có phải là số nguyên tố hay không?
a=int(input("Nhap a: "))
def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(a**0.5)+1):
        if(n%i==0):
            return False
    return True
if isPrime(a):
    print(f"{a} la so nguyen to")
else:
    print(f"{a} khong phai so nguyen to")

# Viết chương trình in ra tất cả số chẵn trong khoảng (M,N) . N, M nhập từ bàn phím.
M=int(input("Nhap M: "))
N=int(input("Nhap N: "))
print(f"Cac so chan trong khoang ({M}, {N}):")
for i in range(M, N+1):
    if i % 2 == 0:
        print(i, end=" ")

a=input("Nhap a: ")
count=0
for letter in a:
    count+=1
print(f"Chieu dai chuoi {count}") 

a=input("Nhap a: ")
count=1 if a else 0
for letter in a:
    if(letter==" "):
        count+=1
    else:
        count
print(f"So luong tu {count}")
