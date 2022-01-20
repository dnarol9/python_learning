print("="*75)
print("*DICTIONARIES*")
print("="*75)
data = {'kushal': 'fedora', 'kart_':'Debian', 'Jayce':'Mac'}
print(data)
print(data['kart_'])
data['parthan'] = 'Ubuntu'
print(data)
del data['kushal']
print(data)
print('soumya' in data)
print(dict((('Intian','dehli'),('bangladesh','Dhaka'))))
data = {}
data.setdefault('names',[]).append('Ruby')
print(data)
data.setdefault('names', []).append('Python')
print(data)
data.setdefault('names', []).append('C')
print(data)
print("="*75) 
print("*LOOPING OVER DICTIONARY*")
print("="*75)
data = {'Kushal': 'Fedora', 'Jace': 'Mac', 'kart_': 'Debian', 'parthan': 'Ubuntu'}
print(data)
for x in data:
    print(f"Key = {x}")
print("-"*75)
print("*DATA:ITEMS()*:")
print()
print(data)
for x, y in data.items():
    print(f"{x} uses {y}")
print("-"*75)
print("*ENUMERATE()*:")
print()
for i, j in enumerate(['a', 'b', 'c']):
    print(i, j)
print("-"*75)
print("*ZIP()*:")
print()
a = ['Pradeepto', 'Kushal']
b = ['OpenSUSE', 'Fedora']
for x, y in zip(a, b):
    print("%s uses %s" % (x, y))