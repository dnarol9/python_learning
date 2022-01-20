a = [1, 2, 3]
print([x * x for x in a])
z = [x+ 1 for x in[x * x for x in a]]
print(z)
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(any(numbers))
print(all(numbers))
numbers.append(0)
print(all(numbers))