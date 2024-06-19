def calculatedgrade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'


grade = []
students  = int(input("enter the number of students"))
for stu in range(students):
    a,b,c,d,e = (input("enter the marks of 5 subject").split())
    score = (int(a)+int(b)+int(c)+int(d)+int(e))/5
    grade.append(calculatedgrade(score))
print(grade)
