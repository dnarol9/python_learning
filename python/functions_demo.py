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
c = input("start ")
while c == "y":
    i = int(input("Enter number to append: "))
    print(f(i))
    c = input("continue?" )
