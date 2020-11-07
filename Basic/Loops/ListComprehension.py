chars = [l for l in "simpsons"]
print(chars)

values = [i for i in range(0, 11)]
print(values)

numbers = [n-10 for n in range(0, 101) if n > 50]
print(numbers)

l1 = [2,4,6,8,10]
l2 = [-2,4,-6,-8,-10]
pairs = [(x, y) for x in l1 for y in l2 if x+y > 0]
print(pairs)