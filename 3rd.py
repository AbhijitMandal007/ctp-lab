class StudentData:
    # Constructor
    def __init__(self):
        self.students=[]

    # Function to add a student

    def add_student(self):
        student={
            "roll":int(input("Enter roll no : ")),
            "name":input("Enter name : "),
            "age":int(input("Enter age : ")),
            "std":input("Enter standard : "),
            "percent":float(input("Enter average marks in % : "))
        }

        self.students.append(student)
        print(f"Student {student['name']} added successfully\n")


    #Function to Search a student
    def search(self):
        roll=int(input("Enter roll no of the student required : "))
        for student in self.students:
            if student['roll']==roll:
                print("Student's details : \n")
                print(student)
                return

            else:
                print("Student not found\n")

    #Function to Delete student
    def delete(self):
        roll=int(input("Enter roll no of student : "))
        for student in self.students:
            if student['roll']==roll:
                print(f"Student {student['name']} has been deleted from records")
                self.students.remove(student)
                return
            print("Student not found\n")



s1=StudentData()
s1.add_student()
s1.search()