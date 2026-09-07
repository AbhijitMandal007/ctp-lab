import numpy as np


class matrix:
    def __init__(self,mat1,mat2):
        self.mat1=np.array(mat1)
        self.mat2=np.array(mat2)


    def add(self):
        res=self.mat1+self.mat2
        print(f"Addition : \n{res}")


    def sub(self):
        res=self.mat1-self.mat2
        print(f"Subtraction : \n{res}")


    def multiply(self):
        res=self.mat1@self.mat2
        print(f"Multiplication : \n{res}")


    def transpose(self):
            res1=self.mat1.T
            res2=self.mat2.T
            print(f"Transpose of first matrix : \n{res1}")
            print(f"Transpose of second matrix : \n{res2}")



mat1=[
     [2,3],
     [3,5]
]

mat2=[
     [1,0],
     [9,1]
]

obj=matrix(mat1,mat2)
obj.add()
obj.sub()
obj.multiply()
obj.transpose()