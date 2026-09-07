import numpy as np

class Marks:
    def __init__(self,mid,end):
        self.mid=np.array(mid)
        self.end=np.array(end)

    def calculate(self):
        total_marks=self.end.sum(axis=1)
        avrg=self.end.mean(axis=1)
        improvement=(self.end-self.mid)/self.mid*100
        avrg_imp=improvement.mean(axis=1)

        print(f"Total Marks : {total_marks}")
        print(f"Avrage Marks : {avrg}")
        print(f"Percentage Improvement : {avrg_imp}")


mid=[
    [65,70,68,72],
    [78,75,80,77],
    [55,60,58,62],
    [82,85,80,88],
    [70,68,72,74]
]

end=[
    [72,78,75,80],
    [84,82,86,83],
    [65,68,66,70],
    [88,90,85,92],
    [78,75,80,82]
]

obj=Marks(mid,end)
obj.calculate()