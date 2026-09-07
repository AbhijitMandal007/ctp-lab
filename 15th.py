import numpy as np
from scipy.optimize import minimize

def f(v):
    x,y=v
    return (x-2)**2 + (y-2)**2

res=minimize(f,x0=[0,0])

print(f"Minimum value of the function : {res.fun}")
print(f"At x={res.x[0]:.2f} & y={res.x[1]:.2f}")