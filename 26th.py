import matplotlib.pyplot as plt

student=["S1","S2","S3","S4","S5","S6","S7","S8","S9","S10"]
study_hr=[8,10,12,15,18,20,7,14,16,22]
exam_score=[65,72,75,82,88,90,60,80,85,95]

plt.subplot(3,1,1)
plt.hist(study_hr,bins=5,color="skyblue")
plt.title("Distribution of Study Hours")
plt.xlabel("Study Hour/week")
plt.ylabel("No of students")
plt.grid(True)

plt.subplot(3,1,2)
plt.hist(exam_score,bins=5,color="red")
plt.title("Distribution of Exam scores")
plt.xlabel("Exam Score")
plt.ylabel("No of students")
plt.grid(True)

plt.subplot(3,1,3)
plt.scatter(study_hr,exam_score)
plt.title("Study Hour vs Exam scores")
plt.xlabel("Study Hour/week")
plt.ylabel("Exam Score")
plt.grid(True)

plt.tight_layout()
plt.show()