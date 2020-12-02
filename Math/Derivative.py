from sympy import *

#нахождение частной производной по Х
#x, y = symbols('x y')
#result = diff(x**2 + y**2, x)
#print(result)

'''
x, y, z = symbols('x y z')
f = 2*x**2 - 4*x*z + 4*y**2 - 8*y*z + 9*z**2 + 4*x + 8*y - 20*z
resultX = diff(f, x)
resultY = diff(f, y)
resultZ = diff(f, z)
print(resultX)
print(resultY)
print(resultZ)
'''

x, y, z = symbols('x y z')
f = 2*x**2 - 4*x*z + 4*y**2 - 8*y*z + 9*z**2 +4*x + 8*y - 20*z
resultX = diff(f, x)
resultY = diff(f, y)
resultZ = diff(f, z)
print(resultX)
print(resultY)
print(resultZ)