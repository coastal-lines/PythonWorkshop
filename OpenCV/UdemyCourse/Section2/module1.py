import numpy as np

mylist = [1,2,3]
print(type(mylist))

mynparray = np.array(mylist)
#print(type(mynparray))

#int
arr = np.arange(0, 10, 1)
#print(type(arr))
#print(arr)

#double
#empty 2dimension array
arr = np.zeros(shape=(5,5))
#print(arr)

#double
arr = np.ones(shape=(5,5))
#print(arr)

#RND
#???
np.random.seed(101)
arr = np.random.randint(0, 100, 10)

print(arr)
print(arr.max())
print(arr.argmax())
print(arr.min())
print(arr.argmin())
print(arr.mean())

#slice
mat = np.arange(0,100).reshape(10,10)

row = 0
col = 1
print(mat[row,col])

print(mat[row,:])

print(mat[0:3,0:3])