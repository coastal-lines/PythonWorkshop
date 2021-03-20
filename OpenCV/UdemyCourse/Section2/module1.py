import numpy as np

mylist = [1,2,3]
print(type(mylist))

mynparray = np.array(mylist)
print(type(mynparray))

#int
arr = np.arange(0, 10, 1)
print(type(arr))
print(arr)

#double
#empty 2dimension array
arr = np.zeros(shape=(5,5))
print(arr)