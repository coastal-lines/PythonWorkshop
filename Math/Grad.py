from numpy import *

x,y,z = mgrid[-100:101:25., -100:101:25., -100:101:25.]

V = 2*x**2 - 4*x*z + 4*y**2 - 8*y*z + 9*z**2 + 4*x + 8*y - 20*z # just a random function for the potential

Ex,Ey,Ez = gradient(V)
print(Ex)
print(Ey)
print(Ez)