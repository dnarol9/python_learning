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