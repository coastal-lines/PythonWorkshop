my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(2)
print(my_set)

l = [1,1,1,1,2,2,2,2,3,3,3,3]
s2 = set(l)
print(s2)

print(1 in my_set)

s1 = {1,2,3,4}
s2 = {1,2,3,4,5}
print(s1.issubset(s2))
print(s2.issubset(s1))
print(s2.issuperset(s1))

s2 = {5,6,7,8}
print(s1.isdisjoint(s2))

s3 = s1.union(s2)
print(s3)

s1 = {1,2,3,4}
s2 = {1,2,3,4,5}
s4 = s1.intersection(s2)
print(s4)

s1 = {0,1,2,3,4}
s2 = {1,2,3,4,5}
s3 = s1.difference(s2)
s4 = s1.symmetric_difference(s2)
print(s3)
print(s4)

print('=================================')
s1 = {0,1,2,3,4}
s1.remove(0)
print(s1)
s1.discard(45)
print(s1)
s1.pop() #удаляет случайный элемент
print(s1)