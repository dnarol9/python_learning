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
