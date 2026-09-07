import numpy as np


class Statistics:
    def __init__(self,data):
        self.data=np.array(data)

    def calculate(self):
        print("Data : ",self.data)
        print("Mean : ",np.mean(self.data))
        print("Median : ",np.median(self.data))
        print("Standard Deviation : ",np.std(self.data))
        print("Minimun : ",np.min(self.data))
        print("Maximum : ",np.max(self.data))

marks=[78,85,92,67,88,73,95,81,76,89]
temperatures=[28.5,30.2,29.8,31.4,27.9,32.1,30.5]
sales=[12500,13800,14200,11900,15100,14750,16000]


print("Statsitical values for marks list are : ")
obj1=Statistics(marks)
obj1.calculate()


print("Statsitical values for temperature list are : ")
obj2=Statistics(temperatures)
obj2.calculate()


print("Statsitical values for sales list are : ")
obj3=Statistics(sales)
obj3.calculate()
