'''Without Numpy'''

class Matrix:
    def __init__(self,mat1,mat2):
        self.mat1=mat1
        self.mat2=mat2


    def add(self):
        r1=len(self.mat1)
        r2=len(self.mat2)
        c1=len(self.mat1[0])
        c2=len(self.mat2[0])

        if r1!=r2 or c1!=c2:
            print("Invalid Subtraction")
            return
        else:
            res=[[0 for j in range(c1)] for i in range(r1)]
            for i in range(r1):
                for j in range(c1):
                    res[i][j]=self.mat1[i][j]+self.mat2[i][j]

            print(f"Adition \n{res}")

    def sub(self):
            r1=len(self.mat1)
            r2=len(self.mat2)
            c1=len(self.mat1[0])
            c2=len(self.mat2[0])
    
            if r1!=r2 or c1!=c2:
                print("Invalid Addition")
                return
            else:
                res=[[0 for j in range(c1)] for i in range(r1)]
                for i in range(r1):
                    for j in range(c1):
                        res[i][j]=self.mat1[i][j]-self.mat2[i][j]
    
                print(f"Subtraction \n{res}")

    def multiply(self):
        r1=len(self.mat1)
        r2=len(self.mat2)
        c1=len(self.mat1[0])
        c2=len(self.mat2[0])
        if c1!=r2:
            print(f"Invalid Multiplication")
            return
        mul=[[0 for i in range(c2)] for j in range(r1)]
        for  i in range(r1):
            for k in range(r1):
                for j in range(r1):
                    mul[i][j]+=self.mat1[i][k]*self.mat2[k][j]

        print(f"Multiplication : \n{mul}")

    def transpose(self):
        r1=len(self.mat1)
        r2=len(self.mat2)
        c1=len(self.mat1[0])
        c2=len(self.mat2[0])

        trans1=[[0 for j in range(r1)] for i in range(c1)]
        trans2=[[0 for j in range(r1)] for i in range(c1)]

        for i in range(r1):
            for j in range(c1):
                trans1[i][j]=self.mat1[j][i]

        for i in range(r1):
            for j in range(c1):
                trans2[i][j]=self.mat1[j][i]

        print(f"Transpose of first matrix : \n{trans1}")
        print(f"Transpose of second matrix : \n{trans2}")


mat1=[
    [1,2],
    [2,3]
]
mat2=[
    [1,2],
    [2,5]
]
obj=Matrix(mat1,mat2)
obj.add()
obj.sub()
obj.multiply()
obj.transpose()