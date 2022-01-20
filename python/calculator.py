print("ENTER CALCULATION IN THIS FORMAT: + 2 3, * 2 3, / 2 3")
data = input().split()
print(data)
n1 = data[1]
n2 = data[2]
numbers = []
numbers.append(n1)
numbers.append(n2)
numbers = [int(x)for x in numbers]
if "*" in data:
   print(n1,"*" ,n2)
   print(numbers[0] * numbers[1])
elif "+" in data:
    print(n1,"+", n2)
    print(numbers[0] + numbers[1])
elif "/" in data:
    print(n1,"/", n2)
    print(numbers[0] / numbers[1])