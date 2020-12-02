from scipy import optimize

def f(x, y):
    return (2.1-x-y)**2 + (2.9-x-3*y)**2 + (4.1-x-5*y)**2

def f_for_scipy(x):
    return f(x[0], x[1])

result = optimize.minimize(lambda x: f(*x), x0=(0, 0)) 
print(result)