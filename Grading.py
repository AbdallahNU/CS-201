points =[]
marks = []
grades = []

for i in range(4):
    mark = eval(input("Enter course mark: "))
    marks.append(mark)
    if mark >= 97:
        points.append(4.0)
        grades.append("A+")
    elif mark >= 93:
        points.append(4.0)
        grades.append('A')
    elif mark >= 89:
        points.append(3.7)
        grades.append("A-")
    elif mark >= 84:
        points.append(3.3)
        grades.append("B+")
    else:
        points.append(0.0)
        grades.append("F")
for j in range(4):
    print('course{0}, grade= {1}, points= {2}'.format(j+1, grades[j], points[j]))

GPA = (4*(points[0]+ points[1]) + 3*(points[2]+points[3]))/14
print('Total GPA is {}'.format(GPA))