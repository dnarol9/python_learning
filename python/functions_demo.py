print("="*50)
print("Palindrome checker:")
print("="*50)
def palindrome(s):
    return s == s[::-1]


if __name__ == "__main__":
    s = input("Enter a string: ")
    if palindrome(s):
        print("Yay a palindrome")
    else:
        print("Oh no, not a palindrome")


def change(a):
    a = 90
    print(f"Inside of the change function {a}")
print("="*50)
print("Local:")
print("="*50)
def change(a):
    a = 90
    print(f"Inside of the change function {a}")
a = 9
print(f"Before the function call {a}")
change(a)
print(f"After the function call {a}")
print("="*50)
print("Global:")
print("="*50)
def change(b):
    global a
    a = 90
    print(a)
a = 9
print("Before the function call ", a)
print("inside change function", end=' ')
change(a)
print("After the function call ", a)
print("="*50)
print("Default argument value:")
print("="*50)
def test(a , b=-99):
    if a > b:
        return True
    else:
        return False
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(test(a, b))
print("="*50)
def f(a, data=[]):
    data.append(a)
    return data
c = input("start?[y/n] ")
while c == "y":
    i = int(input("Enter number to append: "))
    print(f(i))
    c = input("continue?[y/n] ")
    if c == "n":
        print(f(i))
        break
print("="*50)
print("a²+b²=c²")
print("="*50)
import math
def c(a,b):
    return math.sqrt(a*a + b+b)
if __name__ == '__main__':
    print(c(3, 5))
print("="*50)
print("Higher-order function")
print("="*50)
b = int(input("Enter Value: "))
def givemefive():
    def add(x):
        return x + b
    return add
add = givemefive()
i = int(input("Enter Value: "))
print(add(i))
print("="*50)
print("map:")
print("="*50)
lst = [1, 2, 3, 4, 5]
def square(num):
    return num * num
print(list(map(square, lst)))
print("="*50)
print("args, kwargs:")
print("="*50)
def unknown(*args, **kwargs):
    print(f"We received {len(args)} positional arguments. And they are:")
    for arg in args:
        print(arg, end= " ")
    print("")
    print(f"We received {len(kwargs)} keyword arguments. And they are:")
    for k, v in kwargs.items():
        print(f"key={k} and value={v}")
print(unknown(30, 90, "kushal", lang="python", editor="vim"))