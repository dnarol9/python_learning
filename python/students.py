n = int(input("Enter the number of students: "))
data = {} #data storage
languages = ('physics', 'Maths', 'History')
for i in range(0, n):
    name = input(f"Enter the name of the student {i + 1}: ")
    marks = []
    for x in languages:
        marks.append (int(input(f"Enter mark of {x}: ")))
    data[name] = marks
for x, y in data.items():
    average = sum(y)/3
    print("%s's average: %6.2f" % (x, average))
    if average < 3:
        print(f"{x} failed")
    else:
        print(f"{x} passed")
