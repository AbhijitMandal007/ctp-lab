import numpy as np

class Matrix:
    def __init__(self,mat):
        self.mat=np.array(mat)

    def det(self):
        determinant_value=np.linalg.det(self.mat)
        print(f"Determinant value of the matrix : \n{determinant_value}")

    def inverse(self):
        inverse_mat=np.linalg.inv(self.mat)
        print(f"Inverse matrix : \n{inverse_mat}")

    def rank(self):
        rank_of_mat=np.linalg.matrix_rank(self.mat)
        print(f"Rank of the given matrix : \n{rank_of_mat}")

    def display(self):
        print(f"Actual matix : \n{self.mat}")



mat=[
    [1,2],
    [5,1]
]

obj=Matrix(mat)
obj.display()
obj.det()
obj.inverse()
obj.rank()