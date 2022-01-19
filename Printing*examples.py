print("Design 1")
row = int(input("Enter the number of rows: "))
n = row
while n >= 0:
    x = "*" * n
    print(x)
    n -= 1
print("Design 2:")
n = int(input("Enter the number of rows: "))
i = 1
while i <= n:
    print("*" * i)
    i +=1
print("Design 3")
row = int(input("Enter the number of rows: "))
n = row
while n >= 0:
    x = "*" * n
    y = " " * (row - n)
    print(y + x)
    n -= 1

