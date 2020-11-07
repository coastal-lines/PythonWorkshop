l = [10,20,30,40,50]
for i in l:
    print(i)

for i in range(1, 6):
    if i % 2 == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')

for i, item in enumerate(l):
    l[i] *= 100
    print(l[i])

#tuple unpacking
print('-----------')
persons = [('Paul', 27), ('Sara', 28), ('Richard', 29)]
for (name, age) in persons:
    print(f'{name} is {age} years old')