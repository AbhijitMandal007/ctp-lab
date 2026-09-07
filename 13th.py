import numpy as np
from scipy.integrate import quad

def f(x):
    return x**2 + 3*x + 2

#Numerical differentiation at x=2
x=2
h=1e-5
d=(f(x+h)-f(x-h))/(2*h)

#Numerical integration from x=0 to x=2
integral,error=quad(f,0,2)

print(f"Numerical Drivative at x=2 is : {d:.2f}")
print(f"Numerical Integration from x=0 to x=2 : {integral:.2f}")
print(f"Error in Integration : {error}")