import numpy as np


class Matrix:
    def __init__(self,mat):
        self.mat=np.array(mat)

    def eigen(self):
        eig_val,eig_vector=np.linalg.eig(self.mat)

        print(f"Eigen values are : {eig_val}")

        print(f"Eigen vector : \n{eig_vector}")


mat=[
    [1,2,3],
    [2,3,4],
    [4,5,6]
]
obj=Matrix(mat)
obj.eigen()


