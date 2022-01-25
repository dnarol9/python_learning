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
    