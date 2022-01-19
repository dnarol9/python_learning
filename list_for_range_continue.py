print("Lists:")
a = [ 1, 342, 223, 'India', 'Fedora']
print(a[4])
print(a[-2])
print(a[2:3])
print(a[0::2])
if 223 in a:
    print("true")
else: print("false")
if 'linux' in a:
    print("true")
else: print("false")
print("range():")
print(list(range(1, 5)))
print(list(range(10)))
print("Continue:")
while True:
    n = int(input("Please enter an Integer: "))
    if n < 0:
        continue # this will take the execution back to the starting of the loop
    elif n == 0:
        break
    print("Square is ", n * n)
print("Goodbye")

print("for loop:")
for i in range(0,5):
    print(i)
else:
    print("end")