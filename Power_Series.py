x = float(input("enter the value of x: "))
n = term = num = 1
sum = 1.0
while n <= 100:
    term*= x / n
    sum += term
    n += 1
    if term < 0.0001:
        break
print("No of times %d and Sum= %f" % (n, sum))