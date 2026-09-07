import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#Given data
x=np.array([1,2,3,4,5,6])
y=np.array([6,17,34,57,86,121])

#Quadratic equation a*x**2+b*x+c
def f(x,a,b,c):
    return a*x**2 + b*x + c

#Finding the best values of a,b,c 
coefficient,covarience=curve_fit(f,x,y)

#Displaying the coefficients a,b & c
print(f"a={coefficient[0]:.2f}")
print(f"b={coefficient[1]:.2f}")
print(f"c={coefficient[2]:.2f}")

#Displaying fitted equation
print(f"Equation : y={coefficient[0]:.2f}x^2 + {coefficient[1]:.2f}x + {coefficient[2]:.2f}")

#Plotting the Quadratic exprssion
y_fit=f(x,*coefficient)

#Plot of given data points
plt.subplot(2,1,1)
plt.scatter(x,y,color="red",marker="o",label="Original Data")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Given Data Points") 
#Plot of the Fitted Curve
plt.subplot(2,1,2)
plt.plot(x,y_fit,color="blue",marker="s",label="Fitted Curve")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Quadratic Curve Fitting") 
plt.tight_layout()
plt.grid(True)
plt.show()