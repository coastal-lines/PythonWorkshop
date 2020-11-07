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

print('-----------')
players = dict(Me=90, You=100, She=200)
for item in players:
    print(item)

for k,v in players.items():
    print(f'{k} has rating {v}')

for v in players.values():
    print(v)

print('-----------')
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [2,3,4,5,-9,0,-23,-45, -99]
pairs = []
for x in l1:
    for y in l2:
        if x + y == 0:
            pairs.append((x,y))
print(pairs)