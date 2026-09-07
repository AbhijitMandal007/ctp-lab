class PythonLab:
	def __init__(self,num):
		self.num=num
		
	def factorial(self):
		if self.num<0:
			print("Factorial of negative numbers doesnot exist")
		fact=1
		for i in range(1,self.num+1):
			fact*=i
			
		return fact
		
		
	def isPrime(self):
		if self.num<=1:
			return False
			
		for i in range(2,int(self.num**0.5)+1):
			if self.num%i==0:
				return False
				
				
		return True
		
		
n=int(input("Enter a number : "))
a=PythonLab(n)
print("Factorial of ",n," is : ",a.factorial())
if a.isPrime():
	print(n," is a prime number")
	
else:
	print(n," is not a prime number")


