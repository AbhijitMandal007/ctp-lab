class Statistics:
    def __init__(self,data):
        self.data=data
    def calculate(self):
        n=len(self.data)
        sum=0
        for i in range(0,len(self.data)):
            sum=sum+self.data[i]
        mean_val=sum/n
        print("Mean : ",mean_val)
        temp=sorted(self.data)
        if n%2==0:
            median=(temp[n//2-1]+temp[n//2])/2
            print("Median : ",median)
        else:
            median=temp[n//2]
            print("Median : ",median)
        var=0
        for i in self.data:
            var+=(i-mean_val)**2
        var=var/n
        sd=var**0.5
        print("Standard Devition : ",sd)
        maxi=self.data[0]
        for val in self.data:
            if val>maxi:
                maxi=val

        print("Maximum value : ",maxi)
        mini=self.data[0]
        for val in self.data:
            if val<mini:
                mini=val
        
        print("Minimum value : ",mini)
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