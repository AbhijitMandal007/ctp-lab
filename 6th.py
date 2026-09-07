class StudentData:
    def data(self):
        ipfile= open("data.txt","r")
        opfile= open("res.txt","w")


        for line in ipfile:
            data=line.split()
            name=data[0]
            m1=int(data[1])
            m2=int(data[2])
            m3=int(data[3])
            m4=int(data[4])
            m5=int(data[5])
            print("Name : ",name)

            total_marks=m1+m2+m3+m4+m5
            print("Total marks = : ",total_marks)


            avrg=total_marks/5
            print("Average marks = ",avrg)

            #Grade for each student
            grade=""
            if avrg>=90:
                grade="A"
            elif avrg<90 and avrg>80:
                grade="B"
            elif avrg<70 and avrg>60:
               grade="C"
            elif avrg>30 and avrg<60:
                grade="D"
            else:
                grade="F"


            opfile.write(f"{name} {total_marks} {avrg:.2f} {grade}\n")
            print("Result data written to res.txt successfully\n")
        ipfile.close()
        opfile.close()
obj=StudentData()
obj.data()
