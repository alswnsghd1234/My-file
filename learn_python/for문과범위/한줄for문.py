student = [1,2,3,4,5]
print(student)
students = [i+100 for i in student]
print(students)
print(student)

student = ["iron man", " Thor", " I an groot"]
students = [len(i) for i in student]
print(students)

students = [i.upper() for i in student]
[print(students)]