data = list(input())
if "*" in data:
   print(data)
   n1 = data[1]
   n2 = data[2]
   numbers = []
   numbers.append(n1)
   numbers.append(n2)
   print(n1, n2)
   numbers = [int(x)for x in numbers]
   print(numbers[0] * numbers[1])
elif "+" in data:
    print(data)
    n1 = data[1]
    n2 = data[2]
    numbers = []
    numbers.append(n1)
    numbers.append(n2)
    print(n1, n2)
    numbers = [int(x)for x in numbers]
    print(numbers[0] + numbers[1])
elif "/" in data:
    print(data)
    n1 = data[1]
    n2 = data[2]
    numbers = []
    numbers.append(n1)
    numbers.append(n2)
    print(n1, n2)
    numbers = [int(x)for x in numbers]
    print(numbers[0] / numbers[1])