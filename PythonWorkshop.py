import math

#math
print("\n")
print("math:")
print(2 + 2)
print(5 - 6)
print(6 / 2) #always float
print(2.0 + 1)
print(2*3)
print(2**3)
print(3%2)
print(4%2)
print(1.2*3)
print(round(1.2*3, 2))
print(math.sqrt(4))

#variables
print("\n")
print("variable:")
x = 1
print(x)
x = x+2
print(x)
print(type(x))

#bool
print("\n")
print("bool:")
a = True
print(a)
print(2==2)

#none
print("\n")
print("none:")
x = None
print(x)
x = 5
print(x)
print(x is None)

#string
print("\n")
print("string:")
print("This is a \"string\"")
print('C:\\User')
print(r'C:\User')
print("Line one \nLine two")
str = str("hello")
print(str)
print(str[0])
print(str[-1])
print(str[2:])
print(str[0:3])
print(str[::2])
print("1" + "2") #more expensive than format
s1 = "abc"
s2 = "def"
print("%s %s" % (s1, s2))
print("{} {}".format(s1, s2))

#functions for string
print("\n")
print("functions for string:")
s="My name is Paul"
print(len(s))
print(s[len(s) - 1])
print(s.count('a'))
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.isupper())
print(s.islower())
print(s.find('M'))
print(s.find('P', 5))