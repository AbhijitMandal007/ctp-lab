class Student:
    def __init__(self,id,name,course):
        self.id=id
        self.name=name
        self.course=set(course)

    def info(self):
        return (self.id,self.name)


class CourseDetails:
    def __init__(self,c1,c2,c3,c4):
        self.c1=c1
        self.c2=c2
        self.c3=c3
        self.c4=c4

    def display(self):
        print(self.c1.info())
        print(self.c2.info())
        print(self.c3.info())
        print(self.c4.info())


        #Union of courses
        print("Union : ")
        print(self.c1.course | self.c2.course | self.c3.course | self.c4.course)

        #Intersection of courses
        print("Intersction : ")
        print(self.c1.course & self.c2.course & self.c3.course & self.c4.course)

        #Difference of courses
        print("Difference : ")
        print(self.c1.course - self.c2.course - self.c3.course - self.c4.course)



s1=Student(1,"Suroj",["AI","HTML","CSS"])
s2=Student(2,"Ravi",["AI","HTML","CSS"])
s3=Student(3,"Rohit",["AI","DBMS","CSS"])
s4=Student(4,"Virat",["AI","ML","CSS"])
course=CourseDetails(s1,s2,s3,s4)
course.display()
float()
