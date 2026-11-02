import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sales=[45000,52000,48000,61000,58000,65000,62000,70000,68000,75000,72000,80000]


x=range(len(sales))
#Plotting the data
plt.subplot(2,1,1)
plt.plot(months,sales)
plt.xticks(x,months,rotation=45)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales - Line Chart")
plt.grid(True)

plt.subplot(2,1,2)
plt.bar(months,sales,color="red")
plt.xticks(x,months,rotation=45)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales - Bar Chart")
plt.tight_layout()
plt.grid(True)
plt.show()

#Finding Highest and lowest sales 
print(f"Highest Sales : {months[sales.index(max(sales))]},{max(sales)}")
print(f"Highest Sales : {months[sales.index(min(sales))]},{min(sales)}")
