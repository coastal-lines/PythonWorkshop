"""
#ht1
user = input()
star = '*'
for i in range(0, int(user)):
    print(star)
    star = star + '*'

#ht2
print('enter number')
user = input()
for i in range(0, int(user)):
    if i % 2 == 0:
        print(f'{i} is EVEN')
    else:
        print(f'{i} is ODD')
"""

limit = 10
sum = 0
for i in range(0, limit + 1):
    if i % 3 == 0:
        sum = sum + i
        print(i)
        continue
    elif i % 5 == 0:
        sum = sum + i
        print(i)
        continue
print(sum)