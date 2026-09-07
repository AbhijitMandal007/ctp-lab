class Fibonacci:
	def __init__(self,num):
		self.num=num
	def fibo(self,num):
		if n==0:
			return 0
		elif n==1:
			return 1
		else:
			return self.fibo(n-1)+self.fibo(n-2)
		
n=int(input("Enter a number : "))
obj=Fibonacci(n)
print(n,"th term of Fibonacci Series is : ",obj.fibo())
